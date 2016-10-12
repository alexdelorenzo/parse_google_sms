from setuptools import setup


setup(name="google_voice_parser",
      version="0.1",
      description="Parse SMS from Google Voice",
      url="https://github.com/thismachinechills/parse_google_sms",
      author="thismachinechills (Alex)",
      license="AGPL 3.0",
      packages=['google_voice_parser'],
      zip_safe=True,
      install_requires=["html_wrapper", "click"],
      keywords=["google voice", "voice", "sms", "takeout"],
      )
