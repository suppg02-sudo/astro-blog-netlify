---
pubDatetime: 2026-02-10T19:21:52Z
title: "How to Add Webhooks to trigger.dev Automatically"
postSlug: "add-webhooks-trigger-dev-automatically"
description: "How to Add Webhooks to trigger.dev Automatically"
tags:
  - webhooks
  - workflow-automation
  - modal
  - trigger.dev
  - tutorial
---

In my previous video, I introduced you to trigger.dev and why I believe this framework is going to replace a majority of workflow automation tools as we know them today. If you're already in the workflow automation game, you probably know that you can use AI to create workflows for you. However, there's a big issue: **AI is non-deterministic and doesn't follow specific rules**. So, debugging is really difficult and data often gets lost.

trigger.dev is a framework that can solve that for you. As you can see, it has long-running tasks with retries, queues, observability, and elastic scaling. All of those are features that AI doesn't handle well out of the box, especially if you build no-code apps. This is basically an engine that AI can use to have a programmatic and more deterministic way of creating workflow automations for you so that you don't need to build them manually in n8n.

All of this works incredibly well. However, there's something missing in trigger.dev that others like n8n have: **a webhook integration**.

## The Missing Webhook Problem

If you look at n8n, for example, it has a webhook integration which means that any external service can send information to one specific endpoint in n8n, and it can then use that endpoint information to execute other tasks after. Now while that's amazing, trigger.dev is a bit different because they have an API that you would need to connect. So it's not just that it can take any kind of webhook endpoint or any kind of structured data, but without any specific protocol or norm on top.

You don't necessarily know how the data arrives. You don't really know how to execute that in trigger.dev.

In this video, I'm going to show you two specific ways on how you can use trigger.dev in combination with a webhook setup that allows you to trigger pretty much any kind of service out there that has a webhook endpoint or an API endpoint to get data into trigger.dev and execute it right there inside of a scenario or a task run.

## Two Methods to Add Webhooks

We're going to do this in two specific ways. Number one is that we have a Docker container with a web server which, by the way, is also completely no-code. So all you need is a couple of command lines, and I'm going to show you as well how that works. And we also have a cloud hosted service which is something that is even easier to set up and something we're actually going to start with.

Both of these methods are viable, and I will also explain why I would use which one for what so that you get a better understanding what you should choose if it comes for you to set up webhooks for trigger.dev.

## Getting Started: Fork the Repository

To make sure that you can have a webhook setup that works pretty much out of the box, I have already done the work for you. You'll find this repository in the description below as a download.

The repository is `yanisimo/antigravity-trigger.dev`. And you don't need to get confused or afraid of code that is in there or files because you don't need to touch any of them. I literally just imported this code into Antigravity so that we can use it with our agentic system, and this is exactly what you're going to do as well. You're going to use natural language and a few commands that you just can copy and paste.

### Step 1: Fork and Download

1. Head over to `yanisimo/antigravity-trigger.dev`
2. Open the page
3. Click on **Fork** to create a new fork in your account
4. Download the code (either import the repository or download as a zip file)

You obviously need to have a GitHub account, but I assume at this point you already have one.

### Step 2: Configure Environment Variables

Once you've unzipped the repository, open it in the IDE or agentic system of your choice. That can be Cursor, Windsurf, or Antigravity. Open the `.env.example` file, and you need to adjust a couple of values. These are basically your secrets—the information that you're going to use to connect to all of the accounts.

In this setup, we need a couple of specific things:
- **trigger secret key**: This is the live trigger API
- **staging or development API key**
- **project ID**

The webhook secret is optional. That is something you can use. In the beginning, I would probably recommend not to use it.

### Where to Find Your Keys

You'll find these fields directly inside of trigger.dev. So heading over to trigger.dev, let me just log in here and show you exactly where you will find them.

1. Go down to **API Keys** in the sidebar
2. Within here, you will be able to see the actual keys
3. Copy the key and add it to your `.env` file

You can see this is the development environment. You can then do the same thing for the production environment. Both keys will be in there, and you can simply add them into secret key for production and staging for the development one.

For the last key, you need to copy the project ID, which you will find in the project settings down here. So you click on here, copy this part, and just add this into the project ID.

### Step 3: Create Your .env File

Once you've done that, you simply rename this file to just `.env`. You can see that this is basically the `.env` file that I have already pre-filled with my information. So you don't need to see that. So you simply add your own in here and then basically rename it to `.env` because this file will not be non-existent by default for you.

Now let me just reset that because this is the example you're going to use. But once you have adjusted those, you are pretty much ready to start deploying your webhook setup.

## Method 1: Modal Deployment (Cloud-Hosted)

This is usually the most beginner-friendly method for you and also the cheapest one: deploying it on a cloud hosted service. And there is a service that is incredibly cool. It is called **Modal**, and it is made for deploying AI infrastructure.

Now this doesn't mean anything else than you literally just taking any kind of code and uploading it to a cloud—a server that someone else owns so that you have something that is available in web 24/7. That's kind of like what you need to deploy webhooks, right? If a webhook comes in, you never really know when it comes in. So you want to make sure that whatever service you have is always available and can always receive information on this URL.

### Setting Up Modal

I have already prepared this for you inside of the repository as well. You can see that right here. It is very, very simple. So all you need to do is create an account in Modal, head over to the dashboard, and then in the dashboard, we can basically deploy an app.

1. **Install Modal CLI**: Copy the quick start command and paste it into your terminal
2. **Authorize**: It installs Modal and asks you to create a token for your account
3. Click on **Authorize**, and that's pretty much it

Now we have authenticated this code. You can see here as well it basically stored this information locally in my code which means now we are authenticated. This is pretty much all you needed to do to install Modal on your local system.

### Deploy Your Webhook Server

Inside of this repository, which means now we are ready already to deploy webhooks for trigger.dev. And to do that, there's another line which you will find in here as well.

You can see that down here we have `modal deploy app.py`. This is basically a file we can use. Now if you don't know the exact command for this setup, it would basically just be that you use `modal deploy`. If you don't know that, you can even just ask your agent theoretically because it's built into agent workflows and into documentations. So it knows stuff.

So if you ever get stuck with anything and it doesn't work, you can always ask the agent to help you out with that.

### The Magic Deployment

Other than that, you just copy this same command and press enter. Now, when I press enter, something cool happens. You can see here it does a magic and it deploys it.

If I head back into our Modal dashboard and refresh, you'll see that there is an app that is actually deployed. All right, it looked like Modal actually did an update. So it didn't load for a while, but here we go. It is deployed.

Now I can actually access this page again. You can see it's called `antigravity-hook`. This is pretty much what we just executed right here.

You can see the deployment took **2.4 seconds**, meaning that this app got literally just deployed in 2.4 seconds, meaning at this point of time, it's already in the cloud. That means the whole webhook setup that I created for you is already available in the cloud.

### Accessing Your Webhook URL

If we open this URL now, you will see as well that you get here a deployment URL in a second which you will see when you click here on the FastAPI app, and right in here, you can see this Modal.run URL. This is basically the URL that we can use for webhook endpoint.

When I click on it, it will basically spin up this engine or this specific instance on this server. You can see now it says **"Anti-gravity trigger.dev webhook server is running"**, which means it's live. So whatever we deployed to this webhook or to this server works. And you can see here as well that it automatically launched it.

### Testing Your Webhook

We have this webhook setup ready, and this webhook setup basically allows us to trigger any kinds of things inside of our trigger.dev account because it is basically hooked up inside of custom code that I created here for you to the actual API.

So how can we do that? I have already opened a Postman request here. So we can locally test it. If you don't know about Postman, it is basically a tool that allows me to test webhooks.

So let's say you want to send a webhook from Service A to trigger.dev. You basically send it from Service A to trigger.dev, but this is basically Service A. So I'm just simulating another service to send a webhook from. I'm going to send it as a POST request to the URL that we have available here.

### Finding the Right Endpoint

Let's assume you don't know the endpoint either. We can literally just head into our agent and ask it:

> "I've just deployed a webhook setup and now want to get the exact endpoint for the hello world task. This is the URL that I use for webhook. So I basically just instruct it to create a webhook for Modal based on this specific URL."

And you will now see that the agent goes off. It will basically take the knowledge that it has, it will analyze it, and then it will generate a webhook endpoint for us so that we can basically use it directly inside of Postman to send a demo webhook request. And here we go. It just answered:

> "Webhook endpoint for hello world task is: `https://antigravity-hook--modal.run/webhook/production/hello-world`"

This is the exact URL that we can use, and I can also tell you it uses the production environment. Amazing.

### Understanding Webhook Parameters

So this is exactly what I wanted, and what we can now try. You can see here I have `hello-world`. This is basically a way on how I define webhooks. So just to give you an info up front, there's two variables in here:

1. **Environment**: This file right here is either production or staging. Staging would then basically trigger the same task on the staging environment, and production triggers it obviously on the production environment
2. **Task ID**: As task we have here `hello-world`, this is a representation in the URL

So now we can basically send any kind of information in here. Let me just add an example JSON:

```json
{
  "firstName": "John",
  "lastName": "Doe"
}
```

And I'm going to just send that along within the request to trigger.dev because if you set up everything correctly, including the Modal setup right in here, you can see now it says **success: true**. We have a trigger ID, and we can also see that it actually has been fired.

### Sync vs Async Mode

But you may still ask one more question: "Hey Jannis, this webhook setup works, but where do I see the actual response?" Because you can see that this triggers so it gives a response, but let's for example say you create a webhook where you want to get a response back to that webhook.

n8n for example offers that right when you have an n8n webhook. You can also adjust or manipulate the data that you send back to that webhook. Now this is something that's possible in here as well, which you can do, and you can literally just do that by a parameter that I added.

You can literally just add it in parameters right here. You can either do this with a params tab or you can just add it by yourself. I'll just call it right here in setup.

So in params, I say **mode** and mode can be either sync or async.

- **Async** means you just do the same thing we did right now, which means we don't expect necessarily a response from the actual workflow
- But if I set this to **sync**, I'll trigger the same thing again, and you'll be able to now see in Antigravity here as well as in trigger.dev a new run

So I'm just going to show you that right here. The last run was 6k. If I'm going to trigger this whole thing right here, it now takes a second or a little bit longer to get an answer. But now we will get answer with actual output. So whatever we ran inside of our trigger.dev task is now being returned in here.

### Cost Benefits of Modal

And this is deployed with Modal, meaning that Modal handles basically this whole webhook entry for you, and it has a couple of really, really cool aspects, especially if you're not expecting a massive volume.

That is that you only pay for Modal services that run online when they're actually being used. So in other words, if something is idle or unused, you basically have this deployed here, but there's just no traffic happening back and forth. You are not paying for it.

This is really, really amazing because for smaller services, you may not just want to have a web service that costs you $25 a month or more to run in the background solely for the purpose of maybe like one call a day. And this is basically a service that allows you to handle that directly on cloud compute.

### When Modal Works Best

So you can have literally a deployed service on Modal that just takes the resources that you actually need to execute the task and then you have maybe a bit of time after to downscale it again to zero, which makes it idle again, and then you don't pay again.

It is something you can play around with. And you can see here with this test account, I only spent **1 cent** for pretty much all of the tests that I've done with all of the servers. So it is really, really cheap.

Now, this is the easiest way if you want to get started with it. But in case you have a massive or a tremendous amount of calls, this may not necessarily be the best thing, especially if you downscale at a certain time and it just comes in in big batches because it still scales up or it still has to start itself.

Because obviously if something isn't used, you know for a fact that it's inactive, and that's what you can see here as well in the startup time. The initial trigger of the webhook itself took **3.22 seconds** which means it had to start up this server on their cloud compute so that we can actually use it. Same thing here again you can see that this one again started cold so it took **7.73 seconds** to start.

Now if you have external services and they cancel requests which may happen as well, or they send multiple requests very, very quickly, it can happen that you have to deal with timeouts and stuff doesn't work as well.

## Method 2: Render Deployment (Always-On Web Server)

So if you don't always just want to scale up something from zero, you either need to set it up in here and then again pay more for it and then it may become a bit more pricey if you have something constantly run. And in that case, I would recommend a different setup which is the second setup that I show you now, which is basically a Dockerized setup that allows you to set it up very, very easily on a web server.

I know it sounds complicated, but stick with me. It's going to be very, very straightforward.

### Setting Up Render

We're going to do this with a service called **Render**. Now if you know how to deploy it on Modal, you know that you just get this thing locally, you run command based on file that was created, or you can use even AI to do it. It can really, really help you with that very well, and then you just deploy it on cloud, and that's pretty much it. So you just get a bill for actual usage, and you have your webhook setup in place.

### Creating the Web Service

You could theoretically also deploy both if I think about it. So that's why I'm going to keep this setup on right now because this anyways not costing me any money. But in order for you to get started with Render, you simply head over to render.com and you create an account.

1. Log in and create a **new web service**
2. Click on "New," go to "web service"
3. You will see a page that looks something like this

Now I already have this specific GitHub connected. If you don't, you can simply connect the GitHub account you created earlier to fork this code right here via this button, which then means you will also see the repository that you forked. So it probably called `antigravity-trigger-dev` if you didn't change it.

So if that is the case, all you do is click on here. You wait until it loads, and if everything works out, you should see that it automatically detects something called **Docker**. It's basically something that containerizes your application similar to what happens on Modal. So you know for a fact that if it says Docker right here, you're pretty much good to go.

### Configuring Your Render Service

What you can do then is you can set it to a project if you want to and choose a region. So if you're going to use this system from within Europe, I highly recommend you using Frankfurt as a system to host webhooks itself. Or if you're in the US, you can simply choose any of the other ones.

Now it is a preference or a choice. So if your clients are in the US, it obviously makes sense to have it over there, etc. So it's something that you got to play around with because it introduces a tiny bit more of latency depending on where your service is in the world.

In my case, Frankfurt is perfectly fine. And here, as an instance type, I'm going to take **free** because I just want to test it. Now if you want to run it constantly, I recommend you do that at least with a **starter package**. It will cost you $7 a month, and for the sake of it being a webhook, it is perfectly fine to run it on a $7 per month plan because you most likely don't need to upscale or downscale it.

### Setting Environment Variables on Render

Once you have done that, you still need to set up a couple of environment variables right here. And these are pretty much the same ones you have in your `.env` file. So let's for example say you set up these three variables: trigger secret, staging secret, and project ID.

What you're going to do is you just copy them, you click here on **Add from .env**, you paste them with your actual keys in here, and you click on **Add Variables**. So it would look something like this.

### Deploying and Accessing Your Service

Now once all of that is done, what you simply need to do is click down here on **Deploy Web Service**. Once it's ready, you will see that the web service deploys. It will basically execute all of the code that I shared with you in this GitHub repository, and it will create it on its very own server just for you so that you can use it again in a very similar way like Modal.

The only difference now is that you have it on an actual server, meaning that this one doesn't just downscale by itself and goes to zero. So it is more snappy if you want to.

So rather than this request, for example, if we look at it, it took 4.8 seconds to execute, which is exact time that it took for Modal to basically reactivate whatever code was on there. This one will be a lot quicker, and you can see that in a second once it is deployed.

### Custom Domain Support

Render as well has another really cool feature which is that you can actually add a custom domain. So if you head into settings in here, you scroll down a little bit, you'll be able to see the possibility of adding a custom domain. So you can actually add a custom domain which is really cool. So if you have an own domain, you can theoretically change this URL as well to your own. So it's much easier later to switch things around.

### Auto-Deployment from GitHub

One really, really cool thing that I like personally about Render and it is something you should definitely look into is that it automatically connects to GitHub. So whenever you basically push or adjust something in this code and you maybe want to make sure you can add this code into your repository, so one you fetch, you can version things which means you can basically see at which point you have made which changes.

So you can either revert them, you can adjust them. This is the whole point of GitHub basically. But once you have done that and you can push something into this codebase, Render will automatically deploy it for you. So it will automatically update what's currently in this cloud version so that it can use the latest version without any kind of other technology or technological understanding.

### Performance Comparison

Now let's head over here and just refresh this thing. It may take a while to start, and this is usually initial deployment. So it can take anywhere from a minute to maybe 5 to 10 minutes. Depends a bit on the size of the server. But once it's done, you will see as well here in the events tab that the deployment is ready.

All right, here we go. It just deployed it, which means if we head now to the website, you can see `antigravity-trigger-dev website server is running`. Now interestingly enough, this one shows it as a JSON. This one doesn't. And the reason for that is because it uses actually a different codebase, which means that in here we have two different types of web apps.

You can see we have the normal web app and the Modal one. And the reason for that again is very simple: the web app that we deployed here on Render is actually built in TypeScript. So it is a JavaScript/Node.js-based setup while the setup that we see inside of Modal right here is completely Python-based.

So to be fair, in your specific scenario, this probably doesn't make much of a difference, but it's just important to know when you code. So if you prefer using Python, you may want to just use Modal. Or if you prefer using Node.js, you can also just use any web service. So that's just something to keep in the back of your mind.

### Speed Comparison

However, we are live, and we have already adjusted the URL in here, right? So we can see that the previous one on Modal took 4.8 seconds to run on a cold system. So now if we're going to run this one right here, it should be way quicker.

And it actually wasn't too much quicker here. It's 2 seconds now. I mean good, it's half of it, but in my opinion, I think you can definitely get this even quicker. But one of the reasons why you also think it takes longer is because we have it in sync mode. So it doesn't necessarily just rely on webhook to answer, but it also waits for the actual task inside of trigger.dev to execute.

So if I remove this or let's even say we just set it to async, it should be a lot quicker because then we don't need to wait for the actual trigger to run.

And here we go. You can see now it's **1.7 seconds**. If we're going to run this whole thing again, it should probably be even quicker because it's already warm. Okay, so it's again still around 2 seconds. So I'd say this is still okay because I don't think in the task we have much happening.

If we're going to look at the task runs right here, you should see that the task itself took 830 milliseconds. This one around 700. So this is probably what accounts for roughly a little bit less than half of the time of what it actually takes to execute. But nevertheless, it executes now on web server. So this is basically the exact same setup that we had on Modal, but now running on a web server that is always available and doesn't need to boot up.

## Choosing the Right Method

So first time you're going to call it, it's always going to be quicker, but in the end, as we've seen, it always has the exact same functionality. So this is a way on how you can set up webhooks with trigger.dev, which in my opinion just eliminates the whole need for anyone else.

And if you're already using the repository I shared with you, this is literally exactly what you can use to create any kind of trigger.dev tasks automatically on autopilot by just talking to it in natural language. And that is precisely how you set up webhooks with trigger.dev.

### Modal vs Render: Decision Matrix

| Feature | Modal | Render |
|----------|--------|--------|
| **Setup Complexity** | Simple (few commands) | Moderate (web interface) |
| **Cost Model** | Pay for usage only | Fixed monthly ($7+) |
| **Cold Start** | 3-7 seconds | None (always on) |
| **Warm Response** | ~1-2 seconds | ~1.7-2 seconds |
| **Best For** | Low volume, testing | Production, high volume |
| **Auto-Scaling** | Yes, to zero | Manual instance sizing |
| **Custom Domain** | No | Yes |

## Key Takeaways

1. **trigger.dev provides deterministic workflow execution** with retries, queues, observability, and elastic scaling—features that AI alone cannot provide

2. **Webhooks bridge external services** to trigger.dev automation, enabling integration with any service that offers webhook endpoints

3. **Two deployment paths offer flexibility** based on your specific use case and budget: Modal for cost-conscious, low-volume usage; Render for production, high-volume workloads

4. **Modal is ideal for beginners** and low-cost experimentation, with incredible pay-for-usage pricing (as low as 1 cent for testing)

5. **Render suits production deployments** requiring consistent performance, with faster response times and no cold starts

6. **AI can assist throughout** the entire setup and configuration process, making webhook implementation accessible even to non-developers

7. **Version control and auto-deployment** are built-in features, especially with Render's GitHub integration

8. **Sync vs async modes** give you control over whether to wait for workflow execution and receive results or just trigger and forget

## Conclusion

If you want to learn more about it or understand the exact concept that I have in here a bit more in detail, you can always just talk to AI. You can always ask it how it's supposed to do something because it is defined inside of agents. And if you want to read through it manually, you have a manual right in here. And you even have documentation right in here for webhooks, both for Modal and the actual web service.

So this way you can always know what's going on and how you can potentially fix things. But nevertheless, I anyways recommend most of the time just using AI for it because that's anyways the direction everything goes.

Thank you very much for watching. I hope I could show you some insights. And if you'd like to learn more about it, I highly recommend checking out our community. It's linked below in the description. This is where people start making a living with AI, working remotely, working on their own terms, and just staying ahead of the curve to make sure you have a stable future.

---

## Resources

- **Repository:** [yanisimo/antigravity-trigger.dev](https://github.com/yanisimo/antigravity-trigger.dev)
- **Video Source:** [How I Add Webhooks to trigger.dev Automatically](https://youtu.be/ryfaz9DDkFE)
- **Full Transcript:** `/media/docs/output/youtube_How_I_Add_Webhooks_to_triggerdev_Automatically_ryfaz9DDkFE_20260210_192152.txt`
- **Short Summary:** `/media/docs/output/youtube_How_I_Add_Webhooks_to_triggerdev_Automatically_ryfaz9DDkFE_20260210_192152_summary_short.md`