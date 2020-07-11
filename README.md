![YT Tags Rich Preview](yttags/static/img/yttags-rich-preview-banner.jpg)
--------------------------------------------------------------------------------
# YT Tags
https://yttags.com/

## YouTube Analytics Tools
* [Keyword Research Tool](https://yttags.com/keywords)
* [Tag Finder](https://yttags.com/tags)

## Contributing to YT Tags
Thank you for your interest in contributing to YT Tags! Before you begin writing code, it is important that you share your intention to contribute with the team, based on the type of contribution:

1. You want to let us know about a bug or fix a bug yourself.
    - Post about the problem in an [issue](https://github.com/mmyoung979/yttags/issues),


2. You want to propose a new feature and implement it.
    - Post about your intended feature in an [issue](https://github.com/mmyoung979/yttags/issues),
    and we shall discuss the design and implementation. Once we agree that the plan looks good,
    go ahead and implement it.


3. You want to implement a feature or bug-fix for an outstanding issue.
    - Search for your issue in the [YT Tags issue list](https://github.com/mmyoung979/yttags/issues).
    - Pick an issue and comment that you'd like to work on the feature or bug-fix.
    - If you need more context on a particular issue, please ask and we shall provide.

## Getting Started
After forking, run the following commands to get started:
```
cd yttags/
cp config/settings/production.py config/settings/local.py
python3 manage.py runserver --settings=config.settings.local
```

### Troubleshooting
* Replace environment variables with your own ([you will need a YouTube API Key](https://developers.google.com/youtube/v3/getting-started))
* You can delete the SMTP settings section for now
