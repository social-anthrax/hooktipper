# Hook Tipper

Feel like you don't get paid enough? Feel like american tipping culture should benefit you as well? Always thought that using a table to ask for tips was a genius idea? Feel like doing a git commit don't break enough tools?

No? Unfortunate! With hooktipper you can add a tipping screen as a git commit hook, so every time someone tries to commit they'll get asked to send you money!

![Screen recording of a user running git commit -m 'add git hook' which then causes a tui to appear asking them for a donation. Once the user clicks the $1 option it takes them to a stripe payment page](./README.assets/C9665418-D0B9-4125-A80D-D1B6C265CE53.gif)

## Setup

Simply add the following to your .pre-commit-config.yaml and use [pre-commit](https://pre-commit.com/). Add tip quantities via the args and the link that your generous tipper should visit to pay you. Make sure to add a custom amount too.

```yaml
 - repo: https://github.com/social-anthrax/hooktipper.git
    rev: v0.1.0
    hooks:
      - id: hooktipper
        args: 
        - 1=https://donate.stripe.com/test_fZe01z2PrbfjeuQeUU
        - 3=https://buy.stripe.com/test_6oEeWt2PrervfyUcMN
        - 5=https://buy.stripe.com/test_14k5lT75H0AF5Yk7su
        - custom=https://buy.stripe.com/test_28o29HahTdnrfyUaEH
```
