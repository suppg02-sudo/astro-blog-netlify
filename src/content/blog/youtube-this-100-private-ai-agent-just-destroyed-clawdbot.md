---
pubDatetime: 2026-02-09T00:05:00Z
title: "This 100% private AI Agent just destroyed Clawdbot"
postSlug: "youtube-this-100-private-ai-agent-just-destroyed-clawdbot"
description: "This 100% private AI Agent just destroyed Clawdbot"
tags:
  - VPS
  - Open Source
  - AI Agents
  - AI
  - Agent Zero
  - Privacy
---

## Executive Summary

This 28-minute video by David Ondrej demonstrates how to set up **Agent Zero**, a powerful open-source AI agent that runs on a Virtual Private Server (VPS). Key highlights:

### Key Features of Agent Zero
- **100% Private & Open Source**: Fully open-source project with privacy and security as core values
- **Multi-Model Support**: Works with OpenRouter, Venice AI, and includes free inference through AOT token staking
- **Advanced Features**: Knowledge files, secret management, project isolation, and full computer access
- **Cost Efficient**: Clever model delegation reduces costs significantly compared to alternatives like Clawdbot

### Setup Highlights
- Docker-based deployment on VPS (recommended: Hostinger KVM2 plan)
- Port 5080 for web interface access
- Configuration via docker-compose.yml with custom login/password
- OpenRouter API key integration for advanced models like Opus 4.6

### Advantages Over Competitors
- **Smart Model Delegation**: Use different models for different tasks (chat, utility, web browsing)
- **Secret Management**: API keys stored securely - never exposed to external providers or added to context
- **Project Isolation**: Separate workspaces with project-specific memories and instructions
- **Free Inference**: Stake AOT tokens to get $8+ daily API credits

### Latest AI Model Updates (as of video)
- **Claude Opus 4.6**: Released during recording, better at tool calling and terminal usage
- **GPT 5.3 Codex**: OpenAI's latest coding model
- **Plateau Concerns**: Both models show coding performance plateauing, focusing instead on office tasks and knowledge work

### Recommended Models
- **Chat Model**: Claude Opus 4.6 (powerful, expensive)
- **Utility Model**: Qwen 2.5 or similar (cheap, capable for quick tasks)
- **Web Browser Model**: Opus 4.6 (for complex browsing tasks)

{{< mermaid >}}
graph LR
    A[Start] --> B[Install Docker]
    B --> C[Create docker-compose.yml]
    C --> D[Configure API Keys]
    D --> E[Start Container]
    E --> F[Access VPS]
    F --> G[Configure Models]
    G --> H[Set Up Secrets]
    H --> I[Create Projects]
    I --> J[Stake AOT Tokens]
    J --> K[Free Daily Inference]
    K --> L[Agent Zero Ready]
{{< /mermaid >}}

## Full Transcript

### [00:00] Agent Zero is the most powerful AI agent

Agent Zero is the most powerful AI agent on the market, and putting it on a VPS makes it even stronger. With Agent Zero, you can analyze thousands of files autonomously, edit videos with code, use a browser like a human would, and get free inference for AI models. Agent Zero is the world's first super agent. And it's also open-source, private, and free to use. In this video, I'll show you how to set up Agent Zero on a VPS so that it's running 24/7. But I do have to warn you though, Agent Zero is very powerful. It will do whatever you tell it to do. So, make sure to use it ethically.

### [00:34] Docker Installation

First, we're going to type in `docker-version` to see if we have Docker installed or not. But, as you can see, we don't have it installed. So, we're going to install it from scratch. The first command I'm going to do is a curl command to install Docker. I'm going to leave this below the video so you actually have it too. But, we also need to do one more command for sudo. Now, reason we need a second command is to run the install script. So, first one just downloads it. The second runs the script.

### [01:08] Docker Compose Setup

As you can see, it's going and I think it should be finished. All right, it's it's done. So now we should have Docker. We type in `clear docker-version` again. Let's see if we have it. We do have it. Beautiful. Version 29.2.1. So now type in `cd` right in the root directory. And then we need to create a file. So type in `nano docker-compose.yml`. Enter. This will open nano editor.

### [01:25] Docker Compose Configuration

Now for this, this is probably the most confusing part. I created a GitHub gist. Again, I'm going to leave this below the video. So, you can just open this. But all you need to do is you need to copy the contents of this. So, just highlight everything. Boom. Ctrl + C. Go back to terminal and just paste it in here. All right. So, when you paste these contents from GitHub gist, you need to change three things, right?

First, login and password. Obviously, don't use admin/admin. Use something more secure than this. But then, we also need to replace the OpenRouter API key so that we can use the newly released Opus 4.6 with Agent Zero, and this model is even better at tool calling and at using the terminal which makes it especially good for Agent Zero.

### [02:10] Setting Up API Key

So of course I'm going to show you how to use it. It literally released like 20 minutes ago. So you're getting a super early view of Opus 4.6. So inside of OpenRouter, go to top right keys, create API key "agent-zero-api". Boom. Now do not share API keys with anybody. I'm going to delete mine before uploading video here. I'm just going to paste it in. And then we need to do two commands. Ctrl+O to save and you need to hit enter to confirm the file name and then Ctrl+X to exit nano editor.

### [02:38] Starting the Container

And now we should be able to start Agent Zero. So let me do clear again. And the last remaining command is `docker compose up -d` enter. So now it's going to pull Agent Zero image from Docker. And this is a couple gigabytes. So it might take a while depending on how fast your internet is. And the reason it's a couple gigabytes is because it contains a full operating system inside of it.

### [02:59] Docker Compose Benefits

And the reason we use Docker Compose is so that it's easier to stop and start the container without losing your config. Oh, and by the way, if you don't want to use OpenRouter, later in the video, we'll show you how to get free inference with Agent Zero. So, make sure to watch until the end. And by the way, if you don't have any VPS, what me and my team use is Hostinger. This is where we host all of our VPS servers.

### [03:17] VPS Hosting Recommendation

And personally, I think the KVM2 plan is really solid. You can easily run Agent Zero on this forever. As you can see, you get two VPU cores, 8 gigs of RAM, and 100 GB of disk storage. And it's very, very affordable. So, the reason I use Hostinger is not only is it super easy to set up, but also it's one of the most affordable VPSs out there.

### [03:39] VPS Purchase Process

Let me show you. So, just click on "choose plan", and this will take you to the Hostinger card. Now, here I would recommend you select the 24-month plan to get the best deal possible. Now, if you want an even better deal, just scroll down a bit, go to the right, and click on "have a coupon code" and type in code "David" for another 10% off. Then go to the left, select your server, whatever is closest to you. Operating system here, select "plain OS", and just click on "Ubuntu, latest version". Confirm. This has the most tutorials, most support.

### [04:03] VPS Checkout

Once you click that, scroll back up and click on "continue", which will take you to the checkout page. And all that remains is just filling out your first name, last name, and credit card details to buy your own VPS. And once you purchase your VPS, it might take a few minutes to set it up. As you can see, they say three minutes. So just wait for three minutes and then I'll show you how to install Agent Zero.

### [04:24] VPS Terminal Access

Once your VPS finishes setting up, click on "manage VPS". And this will take you to the Hostinger panel where you can see all the details about your server. But what we need to do is we need to go to top right and click on this terminal button right here. And this will give us access directly to the terminal of the VPS. Also, this setup is bare minimum to make it as simple as possible for you guys. But if you want to make your Agent Zero VPS setup as secure as possible, we just uploaded a more detailed tutorial on Agent Zero YouTube channel which will also be linked below the video.

### [04:53] Container Verification

Right, there it is. Image has been pulled. Now to check which containers are running, just type in `docker ps` and you can see that we have to agent zero image. This container is running based on this image. So there's one last thing we need to do. Go back to your Hostinger panel. Scroll to the bottom to find the IP address of your VPS. Copy that. Open a new browser. paste that in and do colon 5080. That's the port. So that is the last step.

### [05:16] Accessing Agent Zero UI

You paste in the IP address and you do colon 5080. Now you should see the login screen right here. And this is literally the same login that you set in the docker-compose, right? So hopefully you didn't leave it default to admin/admin. Hopefully you changed it. But whatever you put it as doing that right now and you should be able to log in to your Agent Zero that is hosted on a VPS. There we go. It's loading.

### [05:39] Testing Agent Zero

And this is the Agent Zero UI. So, it works. But just to confirm that it works, let's go to new chat and type in a message. "Hey, who are you?" Boom. There we go. It's responding. And we're using Opus 4.6, the latest and greatest AI model in the world inside of Agent Zero hosted fully on a VPS that we own. Yeah, this is crazy. Everything is working. The setup is the hardest part.

### [06:04] Agent Configuration

So, now me and Nick are going to show you how to use Agent Zero to the fullest extent and how to give it access to tools like NanoBanana Pro. So that Agent Zero can really do everything and you can just talk to it in plain English and it runs on this VPS and it can control the whole VPS and do whatever it needs to do.

**Nick**: Hey, I'm Nick. I was the first developer at Vectal and now I'm helping record videos for the Agency YouTube channel and also helping some developer work there as well.

### [06:26] Model Configuration

**David**: All right. So actually I forgot to change the models in the settings. So we're going to do that right now. So if you go into settings on the left, we're going to change to main model as well as utility model.

**Nick**: Okay. Okay, so here in settings, if we click on "chat model", it defaults to OpenRouter and GPT4.1. So we can just search for "Claude 4.6" and copy the model name here or whatever other model you want to use. This is going to be the main model, right, for chatting. But there's also a second section.

### [06:55] Multiple Model Types

**David**: Yeah. Yeah. So here we have chat model, utility model, and web browser model. I'm going to use Opus 4.6 for both chat and web browser model. And utility model, it's best to use something cheaper and smaller because this will do, you know, one-off tasks that the main model tells it to.

**Nick**: And by the way, this is a huge advantage over Clawdbot, aka OpenClaw, which burns way more tokens if you give it access to Opus because it doesn't have clever delegation of models like this. Agent Zero, you can use Opus and it will cost you way less money because you can set up different models for different things.

### [07:30] Utility Model Selection

**David**: Yeah, exactly. So for utility model, I'm going to go with a cheap alternative - Qwen 2.5.

**Nick**: Really good model.

**David**: Which is very cheap yet very capable.

**Nick**: Yes.

**David**: So I'm going to copy this and set it here as my utility model. If we save it, we are now able to interact with Opus 4.6.

**Nick**: Maybe we can send a test message, ask which model it is. We just confirm it.

**David**: Yeah. Yes. Let me just ask "what model are you?"

### [07:57] Agent Self-Awareness

**Nick**: It is. So it analyzed its own config, right? Yeah, it went through the config files to find it out. That's not included in the prompt, but it was able to use its own file system to find out what we set it to. And this is the power of giving a powerful AI agent like Agent Zero full access to computer. It can analyze any files. You don't have to worry that it's going to mess up your operating system or whatever because the whole VPS is for Agent Zero to work with. So even though it wasn't included in the prompt, it analyzed the entire file system and found "okay, these are the models."

### [08:27] NanoBanana Pro Integration

**David**: Yeah, that's really good. So another thing that we can do with OpenRouter is we can get access to NanoBanana Pro.

**Nick**: Or any other model or any other tool you know, go ahead.

**David**: Yeah. Yeah. So here we have this quick start section with some documentation. We already created an API key but we can add this as a secret on Agent Zero.

**Nick**: So we're going to explain the secret management system which also is way more private and secure than other alternatives. In other agents, you just have to send secrets into chat, right? Which is very bad practice. In Agent Zero, it's much better.

### [08:50] Secret Management System

**David**: So here in settings, we have external services and below here we have secrets management. So here we have variable store and secret store. The secret store, we can add any variables here and agent will be able to know variable names but never variable values, right? The values will be hidden from the agent and will not be added to context. So this won't be shared with external providers but it will still be able to use curl or Python to make requests using API keys that we got here.

**Nick**: And by the way, this is just a clear example of one of the core values of Agent Zero as a project, which is privacy and security, right? So Agent Zero is fully built to be private, open source, secure, routable locally, and free to use. And not many other projects can say that.

### [09:51] Adding OpenRouter Secret

**David**: Yeah. So let's leverage this and I'll create an OpenRouter API key variable. "OPENROUTER_API_KEY = " and paste. Should I paste this real quickly?

**Nick**: Yeah. And paste the API key we just generated for this project.

**David**: Now, of course, do not share your API keys publicly, guys. I'm going to revoke this one before uploading the video. We're just making it as easy as possible for you to follow.

**Nick**: Yeah, of course.

### [10:14] Creating Knowledge Files

**David**: So, here we can create a new chat. And here in the quick start section on OpenRouter, I'm going to take Python documentation of how to interact with their API. Copy this and I'm going to tell Agent Zero to create a knowledge file from it. So, here's a piece of documentation on how to make requests to NanoBanana Pro through OpenRouter to generate images.

"I need you to turn this into reusable knowledge. Save this as a markdown file that you can reference."

**David**: So here I'm going to paste the Python code that I copied from the documentation. So you can see it's searching memories here. This is going through the knowledge files that it already has.

### [11:03] Knowledge Storage

**David**: So basically knowledge here in Agent Zero is stored in the knowledge directory in the container and everything that gets indexed and can be searched like a, so you can add your own knowledge files or do like I'm doing here just telling it to save something for later reference and it will have that knowledge on how to generate images.

**Nick**: Yeah. So the model it uses to search memories is the utility model that we set there. So it's using Qwen 2.5 to search the knowledge.

**David**: Yeah, it's using Qwen 2.5 to search the knowledge, and now it's using Claude Opus to generate the final response.

### [11:35] Testing Image Generation

**David**: All right. So now it has a knowledge file of how to generate images. So I can tell it to use the OpenRouter API key secret that I added to generate an image of a flying cat over Dubai. Let's see how it performs this.

**Nick**: Okay, so you can see here it's using the secret without ever exposing the actual value. Right? So this is how agent sees secrets. It sees the secret keyword and then the variable name without ever adding that to context. Let's see.

**David**: You're never linking your API keys to external providers like OpenAI, Anthropic, Google, whatever you use. Your API keys stay private on your machine.

**Nick**: Yeah, exactly. Okay, so it created two variants. Let me download one of them. Oh, there it is.

**David**: And here it is - flying cat over Dubai.

**Nick**: Nice. So, even though it doesn't have a built-in NanoBanana Pro, you can easily tell it to do it and it'll just use a terminal command with curl and basically create its own tool. This is the power of giving an AI agent full access to Linux. It basically has unlimited tools.

### [12:45] Extending with External APIs

**David**: Yeah. And you can do this with any external API that you want. You can copy documentation, paste it as a reference, and add secrets in the secret store, and then your Agent Zero can use it.

**Nick**: Okay, so one mistake I see it did when saving the knowledge file, it saved it to `/root/openrouter-image-generation.md` when it's still able to find that file if it needs to. But the right place to save knowledge is into `/ao/user` folder that David showed how to map.

### [13:15] Knowledge File Organization

**David**: Okay, so when David showed you this this gist, you see that we were mapping some folder here `/root/agent0` to this `/ao/usr` folder and this is the place of all of the user-owned files in Agent0. So I want to tell Agent Zero to move that document from there into the user folder.

"Move our knowledge file openrouter markdown instructions from root to `/ao/user` without `e` just `/usr/knowledge` create that directory if needed"

**David**: And by the way, this is for files that are important that need to be referenced exactly multiple times because Agent Zero already has vector database. Right? So yeah.

**Nick**: If something is stored that doesn't need to be referenced word for word, it can just pull up these chunks automatically. Like you can see that now it's searching memories, right? It's doing that with retrieval.

**David**: Yes. And it will automatically index any file that's in this `/ao/user/knowledge` directory. So you can adjust your knowledge files there, right? And that's where this memories are saved as well. So you can see it used a tool called `memory_save` and that's what it used to move it to `/ao/user/knowledge`.

### [14:30] Correcting Memory Path

**David**: So now it did the correct way. Okay. So it updated memory correctly and now it knew to use the memory save tool. So I think if I prompted to save this as a memory, it's better to just say "remember this" like I did before, right? If I say "save this as a memory", it will already use the right path.

**Nick**: Yeah. So now that we already have the OpenRouter API key, another thing that we can do is add Perplexity Deep Research.

**David**: So if you search for "deep research" on Deep Research here, since both of these are OpenRouter so we already added OpenRouter API key. So it's very easy to extend Agent Zero and give it more powers.

**Nick**: Right? So now we can give it Deep Research. So it already can create the best images with NanoBanana Pro. Now we give it Deep Research for Perplexity. So you don't have to use Google AI Studio. You don't have to use Perplexity. Agent Zero will have all of these powers in it.

### [15:26] Adding Deep Research

**David**: Yes, exactly. So we can do even same things. You can go here to Quick Start, get Python documentation, and go back to Agent Zero. Say "now we'll save a new memory in knowledge folder for how to do deep research for Perplexity. I can say also use OpenRouter here."

**Nick**: We're just going to paste in this documentation. The idea is basically right, it just has to use the right model, that's why I'm telling it to create a separate memory. Or use Perplexity for deep research this will also make it trigger this memory when I tell it to do deep research search even though I don't mention OpenRouter explicitly, right. So you can see it's setting some usage and best practices as well in the memory so it knows how to use it efficiently.

**David**: Okay, and use memory save to remember how to do that in future.

**Nick**: Boom, and now it knows how to do deep research. We can test it out. What should we deep research here?

**David**: Latest Opus 4.6 model.

**Nick**: Oh yeah. Okay. So we can test it out. So let me just tell it to search, do a deep research on the latest Opus 4.6 model including benchmarks and relevant news.

**David**: It literally came out like 1 hour ago. So you're getting a fresh latest scoop, guys.

**Nick**: Yeah. And you can see it's using our knowledge, our memory that we just created, and using the secret without ever exposing it. So everything is working as expected here.

### [16:52] Latest AI Model News

**David**: Yeah. So if you care about privacy and security, you really shouldn't be using anything else other than Agent Zero. All right, that's crazy guys. We just got another news - GPT 5.3 Codex released as we're recording this. So both Anthropic and OpenAI released their latest and greatest models. Now what's interesting is that they're taking a different strategy. Anthropic is going after office tasks and knowledge work. They even hit SWE-bench verified from benchmarks.

**Nick**: But GPT 5.3 Codex is obviously about code. So let's scroll down. Nick, is there any coding-related benchmarks here because I think...

**Nick**: Yeah, it says SWE-bench.

**David**: Yeah, that's the first thing they show. So very different approach, but look at this - it's plateauing. That's not a good sign there.

**Nick**: But this is the first.

**David**: Very close to 5.2 too.

**Nick**: Yes, but at least way less tokens though. You can see that output tokens are like nearly half. So it's going to be way more price efficient.

**David**: But there is some sort of plateau going on in the coding side, right? The terminal bench is really good improvement. Same with other tool calling and human-last exam as well. But it's interesting that both of these companies cannot really show large coding gains.

**Nick**: Yes. I think they're both focusing on like knowledge work and computer tasks. Even though this model is named Codex, which should suggest it's coding.

**David**: Jump in coding isn't that big. And same with Opus 4.6. Actually, Opus 4.6 is a little bit worse than Opus 4.5 on SWE. Obviously, overall, it's going to be better because it's better on many other benchmarks, but we are seeing some level of plateau and that's not good news for the stock market, which is already in a nose dive.

### [18:29] Computer Use Improvements

**Nick**: But at least all of these improvements in computer use are good for use with Agent Zero. So that will improve efficiency a lot.

**David**: Yeah, for sure. All right, let's stick with Opus though. People already know how to change models. And here is the output of deep research. So look at this. Look at the length.

**Nick**: Professional services and knowledge work. So it found out the thing that we found as well researching. Yeah, look at this.

**David**: This is Perplexity Deep Research executed by Agent Zero. So you don't even have to use Perplexity. You can just tell Agent Zero, "here's the API key, here's how to use it", and it will use it.

**Nick**: Yeah. 1 million token by way of key highlights.

**David**: Huge release - 1 million token context window.

**Nick**: Okay. So right now I did everything in the root directory and that's because we haven't ever created a project here.

### [19:12] Project Management

**David**: So in Agent Zero we have this projects feature where we can create, you know, projects to separate our work. And each project you can give a name. I'm just going to call this "agent-zero-instance".

**Nick**: And if you're familiar with projects inside of ChatGPT, it's similar but even more powerful because you have their own directory.

### [19:29] Project Features

**David**: Yes, exactly. So we can set instructions here - just a description of what the project is, and instructions that will get appended in the system prompt. So this way you can extend the system prompt of Agent Zero depending on the project that's selected. And here you can enable project-specific memory, and if you do this, all of the memories that were created in the knowledge will be exclusive to the project and it won't route context of other projects and other places that you're working on.

### [19:59] Project Configuration

**Nick**: And you can also configure file structure right, so here you can tell it how it's going to structure files within its project directory. So remember Agent has access to computer, so it will create folders and files, and here you can structure what files are which, you can add documentation here for what's important, and you also have the same secrets store but for projects, right? So you can have a different OpenRouter key for this specific project and this will take precedence over general secrets.

**David**: So for example, set up Agent Zero for a company and then have different projects for different people, and set different API keys and instructions for different employees with each one being a different role at your company.

**Nick**: Exactly.

### [20:40] Advanced Project Features

**David**: Yeah. So, as you can see guys, the project feature is way more advanced than any other AI agent, right? Like nobody has detailed projects like this.

**Nick**: Yeah. And you can see here that it's created a folder in the `/ao/projects/` folder that we mentioned inside projects. And here's the project name. So all of the outputs that we tell it to generate will now be organized in this folder rather than in the root's directory.

**David**: Save this. And then one interesting thing about projects as well is that you can activate them at any point. So here in the chat that we are in, we can switch between projects, right? And we can start in a project but then switch to a different project if we have to do some different type of work.

### [21:21] Project Switching

**Nick**: For instance, if we had a coding project but then we need context of that conversation for content creation, we can switch to a content creation project without losing conversation history. And again, most tools and AI agents don't let you do this. You have to create a new chat if you have to switch to other project. You cannot do advanced context engineering like this.

**David**: Yeah, that's true.

### [21:41] Free Inference with AOT

**David**: All right. So, now we're going to show you how to actually get free inference with the Agent Zero API.

**Nick**: Yeah. So, that's another thing that you can do. Agent Zero has its own token, and utility of AOT token is for distributed governance. So this allows people to vote on future features and you know decide a bit of the way the project's heading, and also we offer free inference through the Agent Zero API.

**David**: Yeah. We also like never promote this so very few people know about this, but now we're going to show you how you can get free inference if you hold Agent Zero token.

**Nick**: Yeah. So you'll need a MetaMask wallet or actually any Web3 wallet installed and some AOT in your wallet. But then once you come here to the Agent Zero site (agent-zero.ai), you're going to link to the Agent Zero website below the video.

### [22:25] Wallet Connection

**David**: And here at the top right, you can click to connect your wallet and this will bring up the Web3 connector and you can sign in, and this will bring up MetaMask or any Web3 wallet that you use. So you have to unlock and confirm this. And here it will automatically detect how much AOT you have.

### [22:40] AOT Staking

**Nick**: And you'll see that we have the option to stake some value in AOT, right? So staking is what allows you to get free inference. You get free inference based on how much AOT you have staked. And here, if you click "add stake", you'll see a form. You'll be brought to a form. I encourage you to read all of the terms and, you know, follow this through mindfully.

**David**: And you can choose how much to stake based on your current balance. And then you can choose lock time. So you can lock this stake for longer and this will increase your stake score, right? So if you lock it for no time, you can withdraw it at any point, but then your stake score will be exactly the amount of AOT you staked. But if you increase this, your lock time, your stake score will be multiplied.

### [23:25] Lock Periods

**Nick**: But if you lock in project, you can lock your tokens for, you know, half a year, a year, and you'll get more inference because of the multiplier.

**David**: Yes, exactly. Just be mindful that this will prevent you from withdrawing these funds, right? That's what makes this powerful. And then you can just create allowance on your wallet to approve this. Going to confirm, and in a second it will detect it here in the Agent Zero website. This reads the blockchain in real time. So it will confirm as soon as it hits the blockchain. You can see allowance is ready and we can continue.

### [23:54] Confirming Stake

**David**: Okay. So when you reach here, you can just hit "stake now" and approve it in your MetaMask wallet. I'm not going to restake it because I already have some AOT staked. If I close it, you see I have 41 AOT staked.

**Nick**: So if you go back, staking is what gives you inference.

**David**: Yes, exactly. And you can stake without locking it and you'll still get free inference, but of course locking it multiplies value, right?

**Nick**: Yes. So this is our way of adding utility to the token.

**David**: Yes, exactly. So here in the website at the top right, you can click your wallet and click "API dashboard". And you'll see I have $8 of free daily API credits, which is not a small amount, right?

### [24:31] Daily Credits

**Nick**: Like if you think about it, unless you're using the most expensive models like aggressively, you can, you know, if you're using like Qwen 2.5 and Gemini 3 Flash and like powerful models that are more cost efficient than Opus, you would basically never run out.

**David**: Yeah. Using Qwen 2.5, I've never hit my daily quota with this amount.

**Nick**: Yes.

**David**: So that's a crazy idea. Like instead of people paying $200 a month for OpenAI, $200 a month for Claude, if you stake some AOT, you can have free daily inference and use basically models that are just as powerful for like next to nothing. So here you can scroll down and you'll see there's an LLM API key. If you don't have it, you have a button to generate it and you can generate that.

### [25:16] Venice AI Integration

**David**: So then you can copy this API key you see here and go back to Agent Zero and in settings in external services, same way we set OpenAI API key we have this "Agent Zero Venice AI" at the beginning and we can paste that key here.

**Nick**: Yes. So paste that in - first Agent Zero Venice API.

**David**: Yes. And then we can save that and oh, actually back in settings we need to change models. Right. Right. So we can use any AI model that Venice offers. Venice offers and they have a lot of open source models but they also have bigger models like Gemini 3 Pro, Claude Sonnet 4.5, Opus 4.5.

**Nick**: Yeah, they basically have all models coming.

**David**: Yeah, 4.6 will be there in a few days for sure.

**Nick**: Yeah. So I'm even going to demo it with Claude Opus to show you guys.

### [26:05] Testing Free Inference

**David**: So back in Agent Zero.

**Nick**: So it's not like you have to use bad models, right? Let's make it very clear. You can use the best possible models when you hold AOT and when you stake it and you get daily free inference.

**David**: And if you want to save some costs even using this, bigger models, you can lower context window here. So you don't spend, you know, long context message history, but you can still get value out of models. Oh yeah, and here we also need to change provider. So the first one, Agent Zero of Venice AI, is what will enable us to use free inference. And you can also change the utility and browser model, but I'm just going to leave it on OpenRouter to test.

### [26:43] Final Test

**David**: And I'm going to tell it to summarize our conversation so far. And we'll see it's...

**Nick**: Maybe check the dashboard out so we can see your credits or quota.

**David**: Dashboard. Okay. Didn't even use anything yet. Okay. Okay. So, I ask it to give me a summary of our conversation and it's accurately summarizing it with our free inference from the Agent Zero API.

**Nick**: Go back to the API dashboard and refresh it. You can see I used just a small amount.

**David**: Yeah, because we use Opus. It's obviously the most expensive model, but yeah, this is how you can use Agent Zero for free. If you hold some tokens, you can stake them on the website and get daily free inference. And most people don't even know about this because we don't want to promote the token and you know turn it into a crypto project. So we focus on the AI side and making a great product. But if you do want to participate and have some utility, this is how you can get free inference.

### [27:37] Privacy Guarantees

**David**: Oh, and another thing about the Agent Zero API is that we do not train on your data. So unlike OpenAI and Anthropic, we don't train AI models on your data and we don't even store any chats. So Agent Zero API is fully private, completely secure, and this is the whole principle of Agent Zero. It's built to be an open source project with privacy in mind, security in mind, that is runnable locally, and that is free to use. So we will never steal your data and we don't even train models, nothing like that, which is something that obviously every other company does.

**Nick**: And yeah, that's it. This is how you can run Agent Zero on a VPS. So if you enjoy this video, make sure to subscribe and I wish you guys a productive week.

---

## Source

- **Video**: [This 100% private AI Agent just destroyed Clawdbot](https://www.youtube.com/watch?v=45-Y8I_Nn4I)
- **Author**: David Ondrej
- **Duration**: 28 minutes 17 seconds
- **Agent Zero**: [agent-zero.ai](https://agent-zero.ai)
- **Recommended VPS**: [Hostinger](https://hostinger.com) (KVM2 plan, use code "David" for 10% off)