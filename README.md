# save-slack-custom-emojis

Tutorial :

1. Get a token _via_ DevTools (may found as `token` in some request parameter)
1. Go to https://api.slack.com/methods/emoji.list/test
1. Execute request with previously found token
1. save JSON result
1. Execute `./downloadEmojis.sh emojis.json`
1. 🎉 All your emojis are now on disk 🎉
