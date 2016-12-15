---
title: Moving away from Evernote
layout: post
---

Evernote has recently [updated its privacy policy](http://arstechnica.com/tech-policy/2016/12/evernotes-new-privacy-policy-raises-eyebrows/) to allow their staff to look at any content you create on their note taking product. They also allow what people are currently calling “machine learning” (Normally bias encoding ‘if-statements’ that bring all the investors to the yard. [The deep-fat fryer of the tech world](http://idlewords.com/talks/deep_fried_data.htm)), but you can opt-out of this if you want.

This bothers me for a few reasons.

Firstly, I like to make the assumption that any information I give to a 3rd party will end up being public one day. Sometimes this is ok, like on Twitter or this blog, but other times are more confusing.

I like to have a clear understanding of what a service is doing with my data, so that I don’t have to constantly evaluate each piece of information I create on each service.

I made my Facebook profile public for this reason: from that point on I didn’t need to worry about privacy, I just didn’t put anything up there that I wasn’t happy to be in the public domain.

I previously trusted (maybe wrongly) that Evernote would take care of my information. This move by them has made it clear to me that they see their business not as a note taking product rather as a platform that allows them to learn about how people write. This in turn allows them to build services using that data. Your content is the product for other services, the note taking app is just the way of generating it. This isn’t what I want from a platform, I want focus on note taking. The risk of my notes being seen by others is much higher now.

Second, and maybe more importantly, I know a lot of people who use Evernote to store very sensitive information. A lot of this is in the public sector research community who do an amazing job of talking to real people about how they interact with the state every day. The work they do to condense these stories in to an abstract understanding of how a well iterated service should start life is one of the main reasons we have such excellent public digital services in the UK.

Notes from the interviews, necessarily, contain very personal content. I hope that no one is writing real names next to these notes, but even so, I bet that a lot of people would be identifiable from the notes alone. Imagine the notes on people who have been interviewed for a devoice service. Or a health related service. This is sensitive stuff.

The idea that a US based, VC backed startup (who apparently won’t be motivated to maintain privacy) can read these notes without notifying the author worries me.  To be clear, I don’t make these notes myself, but as I’ve worked in the public sector a lot it’s easy to imagine that I would have access to them. If I used Evernote every day, I would have to remember that nothing I put in there is private.

Of course, Evernote does have an encryption feature, but I would have to remember to do this for each and every note I created.

So I decided that I needed to move to a system that allows me to write notes in a way that keeps the control and ownership of my data in my hands, not the hands of a company interested in making money out of it.

## My setup

I evaluated a few things when moving away from Evernote:

* Privacy (obviously)
* Open standards that prevent lock in (so that I can move to different software in future)
* Online backups
* Nice authoring environment
* Ability to group notes in to folders
* Platform agnostic

I don’t really need much more than this, but I understand that Evernote does a lot more.

After a bit of looking around I settled on using [Ulysses](https://ulyssesapp.com/) for authoring. I like it because I can write Markdown and save them as text files on by file system, meaning that I can use other editors if I want.

I’ve coupled this with [Boxcryptor](https://www.boxcryptor.com/en) and Dropbox, so that all of my notes are backed up to Dropbox, but encrypted on the way. This means I can access my notes on my phone, but that they are encrypted so that no one else can read them. I’m trying to get iA Writer on my Android phone to write back to Boxcryptor, but I’ve not managed that yet. No matter, I don’t write on the phone anyway. If you use Apple devices then you can use the encrypted iCloud, but I think Apple can decrypt the content of iCloud folders if they want.

In the medium term I will copy [paul_furley](https://twitter.com/paul_furley) and set up my own [Dropbox replacement with Nextcloud](https://www.paulfurley.com/taking-back-my-data-move-from-dropbox-to-nextcloud/).

I’m 24 hours in to this setup, and this blog post is all I’ve written so far, so this might not really work in the longer term.

## List of alternatives
While talking about this, others have suggested other options. I’ve not evaluated these against my criteria above, so some of these might be as bad as Evernote. In general, you should think about who can access your data, and what they might be doing with it. Unless it’s encrypted properly, you should assume that the information will  be public one day (when the company is hacked, goes bust, pivots, or whatever).

Feel free to send me more of these and I will keep this list maintained.

* [iA Writer](https://ia.net/writer)
* [DEVONthink](http://www.devontechnologies.com/products/devonthink/overview.html)
* [Turtl](https://turtlapp.com/) (optionally host your own server, encrypted by default)
* [Microsoft OneNote](https://www.onenote.com/)
* [Google Keep](https://www.google.com/keep/)
* [AudioNote](https://luminantsoftware.com/iphone/audionote.html)
* [Bear](http://www.bear-writer.com/)

## Migrating
Evernote allows you to export your notes to a custom XML format called `ENEX`. Lots of the software linked to above support importing from that format, or there are some other tools that allow converting it to plain text that should mostly work with a new system.

This is a good point to make the case for not using proprietary formats, as you’ll end up getting locked in to the software you’re using. If you keep your notes in text files on a file system, it’s very hard to get locked in.
