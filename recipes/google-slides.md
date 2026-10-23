# Recipe: Google Slides

Two ways in. Both end with an editable Google Slides deck in the kit's layouts, and Google Slides has Space Grotesk and Space Mono built in, so nothing is installed.

## From the pptx

Build `decks/<talk-slug>.pptx` with [pptx.md](pptx.md). Upload it to Google Drive, open it, and choose File > Save as Google Slides. The layouts, backgrounds and fonts come through as they are.

## From the master

For an agent that edits Google Slides directly, or a speaker building by hand: make a copy of the BuidlGuidl master, https://docs.google.com/presentation/d/136xTO2H0B167bFT280bk2gp4YB4F5S2wskYhJqDga1U/copy (the link opens Google's copy dialog), and build in the copy. It has one layout per slide type with the backgrounds, fonts and sizes set, plus an example slide of each. Duplicate the example you want, replace the text, delete the rest. Starting from the master keeps every slide on the kit's layouts.

Highlight a phrase by selecting the words and setting Highlight color to #B5DC3A.

## Look at the slides

Page through the deck in Present mode at full screen, one slide at a time.

## Optional: present from the Devcon link

Devcon gives every session its own Google Slides deck, at a link of the form https://devcon.org/presentation/devcon8/<code>/ that Devcon emails the speaker. Speakers may present from that link or from their own laptop. Devcon's notes monitor on stage works only with Google Slides, so a speaker who wants speaker notes on stage takes this route. To use it, open the Devcon link, choose File > Import slides, pick the deck, select all slides, tick "Keep original theme", import, then delete Devcon's placeholder slides. The kit's slide size is Devcon's, so nothing rescales. Guidelines: https://ef-events.notion.site/Devcon-8-India-Speaker-Guidelines-3e3638cdc41580e2abd8de93aeb659be
