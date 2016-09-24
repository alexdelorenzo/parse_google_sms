#!/usr/bin/env python3

from collections import namedtuple
from datetime import datetime
from glob import glob
from typing import List, Generator

import click
from bs4 import BeautifulSoup


DT_FMT = "%Y-%m-%dT%H:%M:%S.%f"
PRETTY_FMT = "%d %b, %Y %I:%M:%S"
FILE_FMT = "%d_%b_%Y_%I_%M_%S"
SMS_GLOB_FMT = "* - Text - *"


class Sms(namedtuple('Sms', 'time sender msg')):
    def __repr__(self):
        return str(self)

    def __str__(self):
        pretty_date = self.time.strftime(PRETTY_FMT)

        return "[%s] %s: %s" % (pretty_date, self.sender, self.msg)


class Chat(namedtuple('Chat', 'senders msgs')):
    def __str__(self):
        return '\n'.join(map(str, self.msgs))

    def save(self, filename: str = None) -> str:
        if filename is None:
            date = self.msgs[0].time.strftime(FILE_FMT)
            subs = '_'.join('%s' for sub in range(len(self.senders)))
            fmt = 'chat_%s_' + subs
            filename = (fmt + '.txt') % (date, *self.senders)

        with open(filename, 'w') as file:
            file.write(str(self))

        return filename


def read(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()


def get_chatlog_filenames(dir: str) -> List[str]:
    return glob(dir + "/" + SMS_GLOB_FMT)


def wrap_chat(chat_html: str) -> BeautifulSoup:
    return BeautifulSoup(chat_html, 'lxml')


def get_smses(chat: BeautifulSoup) -> List[BeautifulSoup]:
    return chat.find_all('div', 'message')


def parse_dt(sms: BeautifulSoup, fmt: str = DT_FMT) -> datetime:
    dt_str = sms.find("abbr", "dt")['title'][:-6]

    return datetime.strptime(dt_str, fmt)


def parse_sender(sms: BeautifulSoup) -> str:
    return sms.find("a", "tel").text.strip()


def parse_msg(sms: BeautifulSoup) -> str:
    return sms.find('q').text.strip()


def parse_sms(sms: BeautifulSoup) -> Sms:
    time = parse_dt(sms)
    sender = parse_sender(sms)
    msg = parse_msg(sms)

    return Sms(time, sender, msg)


def parse_chat(chat: BeautifulSoup) -> Chat:
    smses = [parse_sms(sms) for sms in get_smses(chat)]
    senders = sorted({sms.sender for sms in smses})

    return Chat(senders, smses)


def gen_chats(dir: str) -> Generator[Chat, None, None]:
    files = get_chatlog_filenames(dir)

    for filename in files:
        yield parse_chat(wrap_chat(read(filename)))


def save_chats(dir: str):
    for chat in gen_chats(dir):
        print(chat.save())


@click.command()
@click.argument("dir")
def cmd(dir: str):
    save_chats(dir)


if __name__ == "__main__":
    cmd()

