---
pubDatetime: 2026-01-27T15:53:41Z
title: "Building a Vercel and Cloudflare Pages Replacement With an $8 VPS"
postSlug: "building-a-vercel-and-cloudflare-pages-replacement-with-an-8-vps"
description: "Building a Vercel and Cloudflare Pages Replacement With an $8 VPS"
tags:
  - devops
  - development
---

# I Built a Vercel and Cloudflare Pages Replacement With an $8 VPS, and It's Faster

*Originally published on [How-To Geek](https://www.howtogeek.com/i-built-a-vercel-and-cloudflare-pages-replacement-with-an-8-vps-and-its-faster/) by Patrick Campanale*

In my quest to launch a SaaS app, I tried out several different hosts, including two of the biggest players for Next.js websites. However, I settled on an unlikely alternative that costs less and delivers more: a VPS. Here's how I ditched Vercel and Cloudflare Pages for my own VPS, and why I think you should too.

## Cloudflare Pages and Vercel offer generous free plans to get started

I have lots of business ideas. I've "started" many businesses over my life, and I always try to find a free way to test the waters before spending money.

With a new SaaS app that I'm working on, I wanted to host it on a scalable platform that would let me start for free and work up from there. I began my journey on Cloudflare Pages because I already use Cloudflare, and it was a simple deployment. Vercel, who created Next.js (the framework I use), also has a free tier that I tried out briefly.

Both free plans actually worked quite well. I could use my own custom domain, handle automated deployments with GitHub, and the page load times were quite speedy. I really have no complaints with either company's free plan, and could have easily launched my SaaS with them, had it not been a few limitations.

## Those free plans eventually run their course

### Sadly nothing free lasts forever

Cloudflare Pages actually has a pretty generous free tier. You get 100,000 requests per day for free, and that's the main limitation. At least, the requests are the main limitation outside package size. On the free Cloudflare Pages plan, you can only deploy up to a 3MB website package. A paid ($5 per month) upgrade bumps your requests up to 10 million per month (with a cost of $0.30 per million after that), and a 10MB package.

The problem is, my SaaS website has enough dependencies that it quickly outgrew the 3MB limit, and even the 10MB upgrade. Once I hit these limitations, I had no choice but to find another service, which is what pushed me to Vercel.

Vercel's free plan is way more generous than Cloudflare Pages, and it's also easier to use as there are no workarounds required to use Next.js. The hobby plan is free forever, gives up to 1 million requests per month, built-in image optimization, and much more. The main limitation that pushed me away from Vercel though was that you can't use the hobby plan for any form of commercial use.

My original goal with my SaaS was to use a free host until I had actual paying users, *then* upgrade. Just installing the Stripe SDK in my webapp was likely to trigger the algorithm and tell Vercel that I wasn't using this site purely for hobby, and it would immediately push me to the $20 per month plan.

Vercel is also known for adding little fees and stuff to the plan, which means the $20 per month plan could easily skyrocket well past that. This comes from the fact that Vercel's billing is entirely usage based without a real way to limit it. Whether it's real traffic, bots, or a bug, if your site needs more resources, Vercel scales and charges for it.

## A cheap VPS offers more capability and costs less

The route that I ended up going with for production, at least, for now, is using a cheap VPS instead of Cloudflare Pages or Vercel. OVH offers pretty well-priced VPS options. I went for VPS-2, which includes 6 vCores, 12GB of RAM, 100GB of NVMe storage, daily backups, 1Gb/s bandwidth, and unlimited traffic—all for $6.75. I ended up paying $7.70 per month for my VPS because I chose to go month to month instead of annual with OVH, but it's still vastly cheaper than other options.

There's little chance my Next.js web app will ever need 100GB of storage, 12GB of RAM, or 6 vCores, but it's there if I need it. Such specs from Vercel would cost approximately over $1,000 per month. Railway (another service I'm checking out, but not sold on yet), would cost $305 per month for the same level of specs that the OVH VPS-2 gives me.

The great part about OVH's VPS system is I can very easily scale without going bankrupt. VPS-6, the highest-tier VPS from OVH before you step into dedicated servers, comes with 24 vCores, 96GB of RAM, 400GB of NVMe SSD storage, and 3Gb/s bandwidth for around $45 per month.

Stepping up from VPS-6 at OVH you can get a dedicated server with an AMD EPYC 4244P, 32GB of DDR5, two 960GB NVMe SSDs, 3Gb/s unmetered public bandwidth and 25Gb/s unmetered private bandwidth, all for $102 per month. Spending $149 per month gets you a dedicated server with the AMD EPYC 4344P, 64GB of DDR5, and the same storage and bandwidth as the other dedicated server.

Basically, the only reason to go with a non-VPS option like Vercel is if you need to mitigate potential downtime by eliminating a single point of failure, as your VPS runs on one specific server. If you need to do updates to the server, or if, for some reason, OVH's datacenter that your VPS is on has problems, your site goes down.

All that to say, I'm spending under $8 per month on a VPS that has fantastic specs, and I can easily scale to running my own dedicated server for less than the cost of Vercel or Railway.

## Coolify is the Vercel replacement I didn't know I needed

One of the things I loved about Vercel, and one of the reasons I really didn't want to leave it, was how simple the deployments were. To deploy my site, I didn't have to FTP or SCP the files to a server and then build or compile, I just pushed to GitHub and the site started building on Vercel. I wanted to be able to do this with my VPS, but wasn't sure how—until I found [Coolify](https://coolify.io/).

The easiest way I can describe Coolify is a full backend dashboard for your server to manage Docker containers, deployments, and more. I have Coolify on my VPS set up so I can deploy through GitHub CI/CD, meaning when I push a change to GitHub, it triggers the site build and deployment on the VPS, just like Vercel did.

However, unlike Vercel, I can also run Docker containers from Coolify. I was able to spin up multiple containers for my SaaS that I would have had to host elsewhere, like Uptime Kuma, Umami analytics, help desk software, and more. Given the specs of the VPS, I have more than enough resources to run the website *and* these containers without having to worry that I'll max anything out.

At the end of the day, a sub-$8 per month VPS offers me more specs than I could ever want. If or when the time comes to grow it, I'll just graduate up to the next VPS level, and keep climbing until I eventually have what's essentially a co-located dedicated server running the app—if it ever comes to that.

---

**Source**: https://www.howtogeek.com/i-built-a-vercel-and-cloudflare-pages-replacement-with-an-8-vps-and-its-faster/