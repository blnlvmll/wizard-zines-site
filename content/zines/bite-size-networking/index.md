---
title: "Bite Size Networking!"
path: /bite-size-networking/
type: zine
date: 2019-03-02
gumroad: https://gum.co/bite-size-networking
twitter: true
ownline: true
---

It's Thursday afternoon and your users are reporting SSL errors in production and you don't know why. Or a HTTP header isn't being set correctly and it's breaking the site. Or you just got a notification that your site's SSL certificate is expiring in 2 days. Or you need to update DNS to point to a new server. Or a server suddenly isn't able to connect to a service.  And networking maybe isn't your full time job, but you still need to get the problem fixed.

Maybe you remember that dig can help you look up your current DNS records, or that to do SSL stuff you can use openssl, or that you can somehow make test requests to look at HTTP headers with curl.  So you spend an hour sifting through Stack Overflow answers, hoping that the one you blindly copy-paste won't wreck anything.

I've been there, but it doesn't need to be this way! It took me literally 2 years to get from "uh what's tcpdump?" to "I've HEARD of tcpdump but I don't really get it" to "well I can blindly copy from stack overflow and sometimes it works" to, finally, "I can easily use tcpdump to debug firewall issues and I always completely understand the commands I run are doing".

Nobody (or almost nobody!) can just flawlessly do every single networking task without ever looking anything up. But!! It's possible to be able to do a lot of basic tasks quickly without always having to look them up. And when you do look something up (as we all do!) you can get to a place where every single time you understand what the command you're typing in does.

This zine explains the 17 most important Linux networking tools, each with a short 1-page comic instead of a 4,000 word man page. For each one, it'll teach you a small number of command line options you need to know to get 80% of your tasks done. (openssl has 47 subcommands, but you probably only need to know how to do 3 things with it. This zine just explains those 3 things ❤). And it'll probably tell you about at least one extremely useful networking tool that you didn't even know existed.

And if you're already comfortable issuing a SSL certificate but you just had 3 new people join your team who have never used openssl (or dig, or curl, or...?) before, then this zine is for you too!  It's easy to get into a situation where more junior folks get stuck because there's nobody around to teach them. Your team can quickly learn some of the basics on their own, and feel like networking tools are accessible and easy to learn. There are corporate rates, and usually you can expense it :). 

Tools in this zine:

* dig
* ping
* curl
* nmap
* netcat
* socat
* tshark
* ngrep
* tcpdump (+ bpf tricks)
* openssl
* mitmproxy
* ssh
* ip
* ss/netstat
* iptables
* tc
* ethtool
* and a page of 20 miscellaneous awesome other tools I love ❤

A few of them are Linux-specific (like ss/ip/iptables). Most work on Mac and BSD too.
