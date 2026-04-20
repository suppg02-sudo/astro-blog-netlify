---
pubDatetime: 2026-02-09T00:02:00Z
title: "This 100% Private AI Agent Just Destroyed Clawdbot"
postSlug: "youtube-45-y8i-nn4i-private-ai-agent"
description: "This 100% Private AI Agent Just Destroyed Clawdbot"
tags:
  - youtube
  - ai-agent
  - privacy
  - venice-ai
  - agent-zero
---

## Summary

This 28-minute video by David Ondrej demonstrates how to set up Agent Zero, described as "the most powerful AI agent on the market," on a VPS (Virtual Private Server) for 24/7 operation. The video covers complete installation using Docker, configuration with OpenRouter API integration, and advanced features like knowledge management, secrets handling, and free inference through Venice AI.

### Key Features of Agent Zero

- **Autonomous Capabilities**: Analyze thousands of files, edit videos with code, use browser like a human
- **Open Source & Private**: Fully open-source, privacy-focused, secure, runs locally
- **Model Flexibility**: Use different models for different tasks (Claude Opus 4.6, Gemini 3 Flash, Kim K2.5)
- **Knowledge System**: Store and retrieve important information from indexed files
- **Secrets Management**: Secure API key storage without exposing values to the agent
- **Project System**: Organize work with isolated contexts per project
- **Free Inference**: Daily API credits available through AOT token staking

### Workflow Overview

{{< mermaid >}}
graph LR
    A[Install Docker] --> B[Create docker-compose.yml]
    B --> C[Configure API Keys]
    C --> D[Start Container]
    D --> E[Access Web UI]
    E --> F[Setup Secrets]
    F --> G[Add Knowledge]
    G --> H[Create Projects]
    H --> I[Stake AOT Tokens]
    I --> J[Get Free Inference]
    J --> K[Use AI Models]
    K --> L[VPS 24/7 Operation]
{{< /mermaid >}}

## Setup Process

### 1. Docker Installation
The video walks through installing Docker from scratch using a curl command and installation script. Once Docker is installed, a `docker-compose.yml` file is created with configuration for Agent Zero.

### 2. VPS Recommendations
The host recommends Hostinger's KVM2 plan:
- 2 VCPU cores
- 8 GB RAM
- 100 GB disk storage
- Affordable pricing

### 3. Configuration Requirements
Three critical settings in `docker-compose.yml`:
- Login credentials (change from default admin/admin)
- OpenRouter API key for model access
- Port mapping (default: 5080)

### 4. Model Selection
Agent Zero supports multiple model categories:
- **Chat Model**: Main conversation model (Claude Opus 4.6 recommended)
- **Utility Model**: Smaller, cheaper model for quick tasks (Kim K2.5 recommended)
- **Web Browser Model**: For web browsing tasks

This clever delegation saves costs significantly compared to Clawdbot, which burns more tokens regardless of task type.

## Advanced Features

### Knowledge Management
Knowledge is stored in `/usr/knowledge` directory inside the container. Files added here are automatically indexed and can be searched by the agent. This allows storing documentation or instructions for later reference.

### Secrets Management
Agent Zero has a superior secrets management system compared to other agents:
- Variable names are exposed to the agent
- Actual values remain hidden
- Values are never added to context or shared with external providers
- Uses secure curl/python requests with stored secrets

### Project System
Advanced project organization allows:
- Separate contexts for different work
- Project-specific instructions
- Project-specific memories
- Isolated secrets per project
- Easy switching between projects without losing conversation history

This enables setting up Agent Zero for a company with different projects for different employees, each with their own API keys and roles.

## Free Inference with Venice AI

By holding AOT tokens and staking them on agent-zero.ai, users receive daily free inference credits:
- Stake tokens to get free daily credits
- Lock tokens for longer periods to increase stake score multiplier
- Use any model from Venice AI (Claude Opus, Gemini, Kim, etc.)
- $8 daily API credits shown as an example
- Never train on user data or store chats

The video emphasizes that most people don't know about this feature, as the team focuses on AI product quality rather than token promotion.

## Recent Model Releases Discussion

The video mentions Claude Opus 4.6 (released ~20 minutes before recording) and Claude 3.7 Sonnet (GPD 5.3 CodeX) from both Anthropic and OpenAI:

### Benchmark Analysis
- Both models show improvements in tool calling and terminal usage
- Coding benchmarks (SWE Bench) show plateauing - not a positive sign for stock market
- Token output nearly halved for efficiency
- Both models excel at knowledge work and computer tasks rather than pure coding gains

This aligns well with Agent Zero's capabilities, which benefit more from computer use improvements.

## Core Principles of Agent Zero

1. **Privacy**: API keys stay on your machine, never shared externally
2. **Security**: No training on user data, no chat storage
3. **Open Source**: Completely open-source project
4. **Local Execution**: Runs on your own hardware
5. **Free to Use**: No subscription required, though AOT staking unlocks free inference

## Conclusion

Agent Zero represents a paradigm shift in AI agents - running entirely on your own VPS with complete privacy, powerful model access through multiple providers, and the ability to use any tool through Linux terminal access. The combination of knowledge management, secrets handling, project isolation, and free inference makes it a compelling alternative to cloud-based AI agents like Clawdbot.

---

## Full Transcript

---

[YOUTUBE TRANSCRIPT]
================================================================================

Title: This 100% private AI Agent just destroyed Clawdbot
Author: David Ondrej
URL: https://www.youtube.com/watch?v=45-Y8I_Nn4I
Video ID: 45-Y8I_Nn4I
Duration: 28m 17s
Language: en
Extracted: 2026-02-09T10:38:13.676395

================================================================================
FULL TRANSCRIPT
================================================================================

Agent Zero is most powerful AI agent on market, and putting it on a VPS makes it even stronger. With Agent Zero, you can analyze thousands of files autonomously, edit videos with code, use browser like a human would, and get free inference for AI models. Agent Zero is world's first super agent. And it's also open- source, private, and free to use. In this video, I'll show you how to set up Agent Zero on a VPS so that it's running 24/7. But I do have to warn you though, Agent Zero is very powerful. It will do whatever you tell it to do. So, make sure to use it ethically. First, we're going to type in docker- version to see if we have Docker installed or not. But, as you can see, we don't have it installed. So, we're going to install it from scratch. The first command I'm going to do is a curl command to install Docker. I'm going to leave this below video so you actually have it too. But, we also need to do one more command for sudo. Now, reason we need a second command is to run install script. So, first one just downloads it. The second runs script. As you can see, it's going and I think it should be finished. All right, it's it's done. So now we should have Docker. We type in clear docker- version again. Let's see if we have it. We do have it. Beautiful. Version 29.2.1. So now type in cd right in the root directory. And then we need to create a file. So type in nano docker-mpose.yamel yiml. Enter. This will open nano editor. Now for this, this is probably most confusing part. I created a GitHub gist. Again, I'm going to leave this below the video. So, you can just open this. But all you need to do is you need to copy the contents of this. So, just highlight everything. Boom. Ctrl + C. Go back to terminal and just paste it in here. All right. So, when you paste these contents from the GitHub gist, you need to change three things, right? First, the login and password. Obviously, don't use admin admin. Use something more secure than this. But then, we also need to replace open our API key so that we can use the new released Opus 4.6 six with agent zero and this model is even better at tool calling and at using terminal which makes it especially good for agent zero. So of course I'm going to show you how to use it. It literally released like 20 minutes ago. So you're getting a super early view of Opus 4.6. So inside of open router go to top right keys create API key agent zero bps. Boom. Now do not share API keys with anybody. I'm going to delete mine before uploading the video here. I'm just going to paste it in. And then we need to do two commands. Ctrl O to save and you need to hit enter to confirm the file name and then Ctrl X to exit the nano editor. And now we should be able to start agent zero. So let me do clear again. And last remaining command is docker compose up dash d enter. So now it's going to pull the agent zero image from docker. And this is a couple gigabytes. So it might take a while depending on how fast your internet is. And reason it's a couple gigabytes is because it contains a full operating system inside of it. And reason we use Docker Compose is so that it's easier to stop and start the container without losing your config. Oh, and by the way, if you don't want to use Open Router, later in the video, we'll show you how to get free inference with Agent Zero. So, make sure to watch until the end. And by the way, if you don't have any VPS, what me and my team use is Hostinger. This is where we host all of our VPS servers. And personally, I think the KVM2 plan is really solid. You can easily run Agent Zero on this forever. As you can see, you get two VPU cores, 8 gigs of RAM, and 100 GB of disk storage. And it's very, very affordable. So, reason I use Hostinger is not only is it super easy to set up, but also it's one of most affordable VPSs out there. Let me show you. So, just click on choose plan, and this will take you to the Hostinger card. Now, here I would recommend you select the 24-month plan to get the best deal possible. Now, if you want an even better deal, just scroll down a bit, go to the right, and click on have a coupon code and type in code David for another 10% off. Then go to the left, select your server, whatever is closest to you. Operating system here, select plain OS, and just click on Ubuntu, latest version. Confirm. This has most tutorials, most support. Once you click that, scroll back up and click on continue, which will take you to the check out page. And all that remains is just filling out your first name, last name, and credit card details to buy your own VPS. And once you purchase your VPS, it might take a few minutes to set it up. As you can see, they say three minutes. So just wait for three minutes and then I'll show you how to install Agent Zero. Once your VPS finishes setting up, click on manage VPS. And this will take you to the Hostinger panel where you can see all the details about your server. But what we need to do is we need to go to top right and click on this terminal button right here. And this will give us access directly to the terminal of the VPS. Also, this setup is the bare minimum to make it as simple as possible for you guys. But if you want to make your Agent Zero VPS setup as secure as possible, we just uploaded a more detailed tutorial on the Agent Zero YouTube channel which will also be linked below the video. Right, there it is. Image has been pulled. Now to check which containers are running, just type in docker ps and you can see that we have agent zero image. This this container is running based on this image. So there's one last thing we need to do. Go back to your Hostinger panel. Scroll to the bottom to find the IP address of your VPS. Copy that. Open a new browser. paste that in and do colon 5080. That's port. So that is the last step. You paste in the IP address and you do colon 5080. Now you should see the login screen right here. And this is literally the same login that you set in the docker compost, right? So hopefully you didn't leave it default to admin admin. Hopefully you changed it. But whatever you put it as doing that right now and you should be able to log in to your agent zero that is hosted on a VPS. There we go. It's loading. And this is the agent zero UI. So, it works. But just to confirm that it works, let's go to new chat and type in a message. Hey, who are you? Boom. There we go. It's responding. And we're using Opus 4.6, the latest and greatest AI model in the world inside of Agent Zero hosted fully on a VPS that we own. Yeah, this is crazy. Everything is uh everything is working. The setup is the hardest part. So, now me and Nick are going to show you how to use Agent Zero to the fullest extent and how to give it access to tools like Nanover Pro. So that agent zero can really do everything and you can just talk to it in plain English and it runs on this VPS and it can control the whole VPS and do whatever it needs to do.

>> Hey, I'm Nick. I was first developer at Vectal and now I'm helping record videos for agency YouTube channel and also helping some developer work there as well.

>> All right. So actually I forgot to change the models in settings. So we're going to do that right now. So if you go into settings in the left, we're going to change the main model as well as the utility model.

>> Okay. Okay, so here in settings, if we click on chat model, uh it defaults to open router and GPT4.1. So we can just search for cloud 4.6 and copy the model name here

>> or whatever other model you want to use. This is going to be the main model, right, for chatting. But there's also a second section.

>> Yeah. Yeah. So here we have a chat model, uh a utility model, and a web browser model. I'm going to use four uh Opus 4.6 for both the chat and the web browser model. And utility model, it's best to use something cheaper and smaller because this will do, you know, uh one-off tasks that main model tells it to.

>> And by the way, this is a huge advantage over Cloudbot, aka OpenClaw, which burns way more tokens if you give it access to Opus because it doesn't have clever delegation of models like this. Agent zero, you can use Opus and it will cost you way less money because you can set up different models for different things.

>> Yeah, exactly. So for the utility model, I'm going to go with a cheap alternative K 2.5

>> really good model

>> which is very cheap yet very capable.

>> Yes.

>> So I'm going to copy this and set it here as my utility model. If we save it, we are now able to interact with cloud 4.6. Um

>> maybe we can send a test message ask which model it is. We just confirm it.

>> Yeah. Yes. Let me just ask what model are you?

>> It is. So it analyzed its own config, right? Yeah, it went through the config files to find it out. That's not included in the prompt, but it was able to use its own file system to find out what we set it to. And

>> this power of giving a powerful AI agent like agent zero full access to computer. It can analyze any files. You don't have to worry that it's going to mess up your operating system or whatever because the whole VPS is for Agent Zero to work with. So even though it wasn't included in the prompt, it analyzed the entire file system and found okay, these are the models. Yeah,

>> that's really good. So another thing that we can do with open router is we can get access to nano banana pro. So here if I go

>> or any other model or any other tool you know go ahead.

>> Yeah. Yeah. So here we have this quick start section with some documentations. Uh we already created an API key but we can add this as a secret on agent zero. So

>> so we're going to explain the secret management system which also is way more private and secure than other alternatives. In other agents, you just have to send send a secret into chat, right? Which is very bad practice. In agent zero, it's much better.

>> So here in settings, we have the external services and below here we have secrets management. So here we have variable store and secret store. The secret store uh we can add any variables here and agent will be able to know variable names but never variable values, right? The values will be hidden from the agent and will not be added to the context. So this won't be shared with external providers but it will still be able to uh use curl or python to make requests using API keys that we got here. And by the way, this is just a clear example of one of the core values of Agent Zero as a project, which is privacy and security, right? So Agent Zero is fully built to be private, open source, secure, routable locally, and free to use. And not many other projects can say that.

>> Yeah. So let's leverage this and I'll create a open router API key variable. Can say this is equals and paste. Should I paste this real quickly?

>> Yeah. Yeah. and paste the API key we just generated for this project. Now,

>> of course, do not share your API keys publicly, guys. I'm going to revoke this one before uploading the video. We're just making it as easy as possible for you to follow.

>> Yeah, of course. So, here we can create a new chat. And here in quick start section on Open Router, I'm going to take Python documentation of how to interact with their API. Copy this and I'm going to tell agent zero to create a knowledge file from it. So, here's a piece of documentation on how to make requests to nano banana bro through open router to generate images. I need you to turn this into reusable knowledge. Save this as a markdown file that you can reference. So, here I'm going to paste the Python code that I copied from the documentation. So you can see it's searching memories here. This is uh going through knowledge uh files that it already has. So basically knowledge here in agent zero is stored in knowledge directory in the container and everything that gets indexed and can be searched like a so you can add your own knowledge files or do like I'm doing here just telling it to save something for later reference and it will have that knowledge on how to generate images. Yeah. So model it uses to search memories is the utility model that we set there. So

>> it's using Kim K2 to yeah it's using Kim K2 to search memories and now it's using cloud opus to generate the final response. All right. So now it has a knowledge file of how to generate the image. So I can tell it to use the open router API key secret that I added to generate an image of flying flying cat over Dubai. Let's see how it performs this. Okay, so you can see here it's using uh secret without ever exposing the actual value. Right? So this is how agent sees secrets. It sees the secret keyword and then variable name without ever adding that to the context. Let's see.

>> You're never linking your API keys to external providers like OpenAI, Anthropic, Google, whatever you use your API keys stay private on your machine.

>> Yeah, exactly. Okay, so it created two varants. Let me download one of them. Oh, there it is. And

>> here it is flying cat over Dubai.

>> Nice. So, even though it doesn't have a built-in Narabana Pro, you can easily tell it to do it and it'll just do a you know terminal command with kernel and basically create its own tool. This is power of giving an AI agent full access to Linux. It basically has unlimited tools.

>> Yeah. And you can do this with any external API that you want. can copy uh documentation, paste it as a reference and add secrets in secret store and then your agency can use it. Okay, so one mistake I see it did when saving the knowledge file, it saved it to uh root/open router image generation.ml when it's still able to find that file if it needs to. But right place to save knowledge is into the / ao/ user folder that David that David showed how to map. Okay, so when David showed you this this gist, you see that we were mapping some folder here root/ aent0 to this A0/usr folder and this is the place of all of the user owned files in agent0. So I want to tell agent z to move that uh document from that into the user folder. So move our knowledge file open router markdown instructions from root to slash AO user user without the e just usr slashn knowledge create that directory if needed

>> and by the way this is for files that are important that need to be referenced exactly multiple times because agent zero already has vector database Right? So yeah,

>> if if something is stored that doesn't need to be like referenced word for word, it can just pull up these chunks automatically. Like you can see that now it's searching memories, right? It's doing that with rack.

>> Yes. And it will automatically index any file that's in this uh AO user knowledge uh directory. So you can adjust your uh knowledge files there, right? And that's where this memories are saved as well. So you can see it used a tool called memory save and that's what it used to move it to AO user knowledge. So now it did it correct way. Okay. So it updated to memory correctly and now it knew to use the memory save uh tool. So I think if I prompted to save this as a memory, it's better to just say remember this like I did before, right? If I say save this as a memory, it will already use to right path.

>> Yeah. Um so now that we already have the open router API key another thing that we can do is add perplexity uh deep research. So if you search for deep research son deep research here

>> yeah since both of these are open router so we already added the open router API key. So it's very easy to make extend agent zero and give it more powers. Right? So now we can give it deep research. So it already can create the best images possible pro. Now we give it deep research for perplexity. So you don't have to use Google AI studio. You don't have to use perplexity. Agent zero will have all of these powers in it.

>> Yes, exactly. So we can do even the same things. You can go here to the quick start, get the Python documentation and go back to agent zero. say now we'll save a new memory in the knowledge folder for how to do deep research for black city I can say also use open router here are the docs I'm just going to paste in this documentation and idea is basically, right it just has to use of right model that's why I'm telling it to create separate memory or using perplexity for deep research this will also make it trigger this memory when I tell it to do deep research search uh even though I don't mention uh open routers explicitly right so you can see it's setting some usage and best practices as well in the memory so it knows how to use it efficiently okay and use memory save to remember how to do that in future boom and now it knows how to do deep research we can test it out what should we deep research here

>> latest OPUS 4.6 model.

>> Oh yeah. Okay. So we can test it out. So let me just tell it to search do a deep research on the latest Opus 4.6 model including benchmarks and relevant news.

>> It literally came out like 1 hour ago. So you're getting a fresh latest scoop, guys.

>> Yeah. And you can see it's using our knowledge, our memory that we just created and using the secret without ever exposing it. So everything is working as expected here.

>> Yeah. So if you care about privacy and security, you really shouldn't be using anything else other than agent zero. All right, that's crazy guys. We just got another news. GBD 5.3 codex released as we're recording this. So both Enthropic and OpenI released their greatest latest models. Now what's interesting is that they're taking a different strategy. Enthropic is going after office tasks and knowledge work. They even hit SWE bench bench verified from benchmarks but GPD 5.3 codex is obviously about code. So let's see scroll down Nick is there any coding related benchmarks here because I think

>> yeah it says SWE bench they

>> yeah that's the first thing they show so very different approach but look at this it's it's plateauing that's not a good sign there

>> but this is first

>> very close to 5.2 too.

>> Yes, but at least way less tokens though. You can see that out tokens

>> are like nearly half. So, it's going to be way more price efficient.

>> But there is some sort of a plateau going on in the coding side, right? The terminal bench is really good improvement. Same with other tool calling and the human last exam as well. But it's interesting that both of these companies cannot really show large coding gains. Yes. I think they're both focusing on like knowledge works and computer tasks. Even though this model is named Codeex, which should suggest it's coding,

>> jumping in coding isn't that big. And same with Opus 4.6. Actually, Opus 4.6 is a little bit worse than Opus 4.5 on SWE. Obviously, overall, it's going to be better because it's better on many other benchmarks, but we are seeing some level of plateau and that's not good news for the stock market, which is already already in a nose dive. You know,

>> but at least all of these improvements in computer use are good for use with agent zero. So that will improve efficiency a lot.

>> Yeah, for sure. All right, let's stick with Opus though. People already know how to change the model. And here is the output of D research. So look at this. Look at the length.

>> Professional services and knowledge work. So it found out the thing that we found as well researching. Yeah, look at this.

>> This is perplexity deep research executed by agent zero. So you don't even have to use perplexity. You can just tell agent zero, here's the API key. here's how to use it and it will use it.

>> Yeah. 1 million tokens by way of key highlights.

>> Huge release 1 million token contacts window.

>> Okay. So right now I did everything in the root directory and that's because we haven't ever created a project here. So in agent zero we have this projects feature where we can create you know projects to separate our work. And each project you can give a name. I'm just going to call this uh agent zero for instance. And if you're familiar with projects inside of CH GBT, it's similar but even more powerful because you have their own directory.

>> Yes, exactly. So we can set instructions here just a description of what the project is and instructions that will get uh appended in the system prompt. So this way you can extend you know the system prompt of agency room depending on the project that's that's selected and here you can enable project specific memory and if you do this all of the memories that were created in the knowledge uh it will be exclusive to the project and it won't route the context of other projects and other places that you're working on. And you can also configure file structure right so here you can tell it how it's going to structure files within its uh project directory. So remember ag has access to uh computer so it will create folders and files and here you can struct it on and what files are which you can add documentation here for u what's important and you also have the same secrets uh store but for projects right so you can have a different open router key for this specific project and this will take precedence over general secrets

>> so for example set up agent zero for a company and then have different projects for different people and set different API AI keys and instructions for different employees with each one being a different role at your company.

>> Exactly.

>> Yeah. So, as as you can see guys, like project feature is way more advanced in than any other AI agent, right? Like nobody has detailed projects like this.

>> Yeah. And you can see here that it's created a folder in the AOSR uh folder that we mentioned inside projects. And here's the project name. So all of the outputs that we tell it to generate will now be organized in this folder rather than in the roots directory. save this. Uh and then one interesting thing about projects as well is that you can activate them at any point. So here in chat that we are we can switch between projects, right? And we can start in a project but then switch to a different project if we have to do some different type of work. U for instance if we had a coding project but then we need context of that conversation for content creation, we can switch to a content creation project without losing conversation history. And again, most tools and AI agents don't let you do this. You have to create a new chat if you have to switch to other project. You cannot do advanced context engineering like this.

>> Yeah, that's true.

>> All right. So, now we're going to show you how to actually get free inference with agent zero API.

>> Yeah. So, that's another thing that you can do. Uh agent zero has its own token and the utility of AOT token is for distributed governance. So this allows people to vote on future futures and you know decide a bit of the way project's heading and also uh we offer free inference through agent zero API.

>> Yeah. We also like never promote this so very few people know about this but now we're going to show you how you can get free inference if you hold agent zero token.

>> Yeah. So you'll need a MetaMask wallet or actually any web3 wallets installed and some AOT in your wallet. But then once you come here to the agent zero site it's agent-zero.ai. AI,

>> you're going to link to Asian zero website below the video.

>> And here at the top right, you can click to connect your wallet and this will bring up the web3 connector and you can sign in and this will bring up MetaMask or any web 3 wallet that you use. So you have to unlock and confirm this. And here it will automatically detect how much AOT you have. And you'll see that we have the option to stake some value in AOT, right? So staking is what allows you to get free inference. You get free inference based on how much AOT you have staked. And here, if you click add stake, you'll see a form. You'll be brought to a form. I encourage you to read all of the terms and, you know, follow this through mindfully. And you can choose how much to stake based on your current balance. And then you can choose to lock time. So you can lock this stake for longer and this will increase stake score, right? So if you lock it for no time, you can withdraw it at any point, but then stake score will be exactly the amount of AOT you staked. But if you increase this uh this lock time, uh your stake score will be multiplied. But if you lock in the project, you can lock your tokens for you know half a year, a year and you'll get more inference because of multiplier.

>> Yes, exactly. Just be mindful that this will prevent you from withdrawing these funds, right? That's what make this makes this powerful. And then you can just create allowance on your wallet to approve this. Going to confirm and in a second it will detect it here in the agency website. This reads the blockchain in real time. So it will confirm as soon as it hits the blockchain. You can see the allowance is ready and we can continue. Okay. So when you reach here, you can just hit stake now and approve it in your MetaMask wallet. I'm not going to restake it because I already have some AOT staked. If I close it, you see I have 41 AOT staked. So if you go back,

>> staking is what gives you inference.

>> Yes, exactly. And you can stake without locking it and you'll still get free inference, but of course locking it uh multiplies value, right?

>> Yes. So this is our way of adding utility to token.

>> Yes, exactly. So here in website at the top right, you can click your wallet and click API dashboard. And you'll see I have $8 of free daily API credits,

>> which is not a small amount, right? Like if you think about it, unless you're using most expensive models like aggressively, you can, you know, if you're using like Kim K2.5 and Gemini 3 flash and like powerful models that are more cost efficient than Opus, you would basically never run out.

>> Yeah. Uh using Kim K 2.5, I've never hit my daily order with this amount.

>> Yes. So that's a crazy idea. Like instead of people paying $200 for a month for OpenAI, $200 a month for C code, if you stake some AOT, you can have free daily inference and use basically models that are just as powerful for like next to nothing. So here you can scroll down and you'll see there's an LLM API key. If you don't have it, you have a button to generate it and you can generate that. So then you can copy this API key you see here and go back to agent zero and in the settings in external services same way we set open AI API key we have this agent zero Venice AI at beginning and we can paste that key here. Okay.

>> Yes. So paste that in the first agent zero Venice API.

>> Yes. And then we can save that and oh actually back in settings we need to change models. Right. Right. So we can use any uh AI model that Venice offers that Venice offers and they have a lot of uh open source models but they also have bigger models like Gymnite 3 Pro you know cloud sonets 4.5 Opus 4.5

>> yeah they basically all models coming

>> yeah 46 will be there in a few days for sure.

>> Yeah. So I'm even going to demo it with cloud opus to show you guys. So back in agent zero.

>> So it's not like you have to use bad models, right? Let's make it very clear. You can use the best possible models when you hold AOT and when you stake it and you get daily free inference.

>> And if you want to save some costs even using this uh bigger models, you can uh lower context window here. So you don't spend you know long contexting message history, but you can still get value out of models. Oh yeah, and here we also need to change provider. So first one, agency of Venice AI, is what will enable us to use free inference. And you can also change utility and a browser model, but I'm just going to leave it on open router to test. And I'm going to tell it to summary of our conversation so far. And we'll see it's

>> maybe check the dashboard out so we can see your credits for quota

>> dashboard. Okay. Didn't even use anything yet. Okay. Okay. So, I ask it to give me a summary of our conversation and it's accurately summarizing it with our free inference from uh agency API. Go back to the API dashboard and refresh it. You can see I use just a s.

>> Yeah. Because we use opus. It's obviously most expensive model, but uh yeah, this is how you can use agent zero for free. If you hold some tokens, you can stake them on the website and get daily free inference. And most people don't even know about this because we don't want to promote token and you know turn it into a crypto project. So we focus on the AI side and making a great product. But if you do want to participate and have some utility, this is how you can get free inference. Oh, and another thing about agent zero API is that we do not train on your data. So unlike OpenAI and Enthropic, we don't train AI models on your data and we don't even store any chats. So agent zero API is fully private, completely secure and this is whole principle of agent zero. It's built to be an open source project with privacy in mind, security in mind that is runnable locally and that is free to use. So we will never steal your data and we don't even train models, nothing like that, which is something that obviously every other company does. And yeah, that's it. This is how you can run agent zero on a VPS. So if you enjoy this video, make sure to subscribe and I wish you guys a productive week.

---

**Source Video**: [This 100% Private AI Agent just destroyed Clawdbot](https://www.youtube.com/watch?v=45-Y8I_Nn4I) by David Ondrej