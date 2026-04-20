---
pubDatetime: 2026-02-09T00:48:27Z
title: "AI Agents Can Now Build Their Own UI in Real Time"
postSlug: "ai-agents-can-now-build-their-own-ui-in-real-time"
description: "AI Agents Can Now Build Their Own UI in Real Time"
tags:
  - agents
  - generative-UI
  - AI
  - personalization
---

## Summary

In this video, Cole Medin explores the concept of **Generative UI** - a powerful paradigm shift where AI agents actively participate in determining what appears on the screen, how information is structured, and how the layout is composed. 

This is not just about AI making recommendations; it's about AI fundamentally reshaping the user interface itself based on user behavior, interests, and context. Medin walks through his complete tech stack, demonstrating how each layer communicates and how agents work with component libraries to deliver truly personalized experiences.

The implications are profound: in the near future, websites like Amazon and Google will look completely different for each user because the entire layout will be personalized based on how they interact with the application and their individual interests.

## Key Takeaways

- **Generative UI Definition**: AI agents play a role in determining what appears on screen, information structure, and layout composition
- **Personalization at Scale**: The future of e-commerce and web applications will feature unique layouts for each user based on their preferences
- **Component Library Architecture**: Agents choose from predefined component libraries and specify props/data through a contract with the frontend
- **Real-Time UI Generation**: The system allows agents to dynamically build UIs in real-time, creating personalized experiences for every user

## Full Transcript

================================================================================

[00:00] Let me show you something really quick.
[00:01] What you're looking at right here is a
[00:03] personalized dashboard that was
[00:05] generated for me based on a bunch of
[00:07] research that my second brain did.
[00:10] Nothing is preconfigured here. It
[00:11] generated the entire layout and chose
[00:14] all of the components completely on the
[00:16] fly. So, we're using an agent for ultra
[00:18] personalization. This is all thanks to
[00:20] generative UI, which if you haven't
[00:23] heard of or used generative UI before,
[00:25] you, my friend, are in for a treat. For
[00:27] the simplest explanation possible,
[00:29] generative UI is the idea that we're
[00:31] going to give our agent the ability to
[00:33] decide the layout and the components for
[00:35] our front end. And with how powerful
[00:37] agents are becoming these days, this is
[00:39] definitely the direction that we are
[00:41] heading. I'm pretty sure in the near
[00:43] future when you go to amazon.com or
[00:45] google.com, exactly what you see is
[00:48] going to look a lot different than the
[00:49] next person because it's going to be
[00:51] personalized to how you use the
[00:52] application and your interests. For
[00:54] example, with this application that I
[00:56] built to demo generative UI for you, all
[00:58] I have to do is paste in any kind of
[01:00] research that my agent did. And then
[01:02] it's going to decide the layout and the
[01:04] components that it thinks is optimal to
[01:06] share this information with me in a more
[01:08] concise way, extracting insights as
[01:11] well. And besides it looking really,
[01:13] really nice, the most beautiful part
[01:15] about this is every single time it
[01:17] generates a dashboard, it's going to be
[01:19] custom to the specific input. And so
[01:21] here's another example. This dashboard
[01:23] looks completely different because it's
[01:25] optimized to what it thinks I want to
[01:27] see. And that's something that I can
[01:28] optimize in the prompts for the agent as
[01:30] well. And the important thing to keep in
[01:32] mind here is this that I built for you
[01:33] is just a single use case to show you
[01:36] the power of generative UI. This really
[01:37] is the future of software. And so we'll
[01:40] get into why that's the case, how
[01:42] generative UI works exactly. I'll even
[01:44] get into the architecture that I've
[01:46] built for this application so you can
[01:48] see how to incorporate it for yourself.
[01:50] And I know there's quite a bit that goes
[01:51] into the tech stack here, but I'll break
[01:53] it down nice and simple for you. And of
[01:55] course, this project to demonstrate
[01:56] generative UI, I'll have as a GitHub
[01:58] repo linked in the description. It is a
[02:00] really good starting point for you to
[02:02] understand generative UI and even build
[02:04] on top of this to create your own
[02:05] application. I put a lot of work into
[02:08] designing a really solid tech stack
[02:10] here. So, I'll get into this more in a
[02:13] little bit, but we have our Pantic AI
[02:15] agent. This is the agent running in the
[02:17] back end that is choosing the components
[02:19] and designing the layout. And then for
[02:21] our generative UI protocol, we're using
[02:24] A2UI from Google. This is the
[02:26] specification exactly how does the agent
[02:29] define the components that we're going
[02:31] to render in our front end. And so we
[02:34] send this over to our front end and
[02:35] we're using the protocol AGUI. I've
[02:38] covered this on my channel before, but
[02:40] this is our way to very easily connect
[02:43] our agent to our front end. And so I
[02:45] know it's a little bit confusing here
[02:46] because we have two protocols. A2UI is
[02:49] for specifying the components and the
[02:51] standard there. AGUI is for connecting
[02:54] our agent running through an API with
[02:56] our front end. And we're using Copilot
[02:58] Kit because Copilot Kit makes it super
[03:01] easy to build these really interactive
[03:03] front-end apps and it integrates
[03:04] directly with all of the other parts of
[03:07] our tech stack. And so we take the
[03:09] requests from the agent. this is what we
[03:11] want to render and then we create those
[03:13] as React components to make that
[03:15] beautiful dashboard that we're
[03:16] displaying to the user in the end. And
[03:18] so we'll get more into how this works,
[03:20] but the first thing that I want to cover
[03:21] with you is generative UI at a higher
[03:23] level. Why is this so powerful and
[03:26] exactly how can you use it for yourself?
[03:28] So we've already covered the most basic
[03:30] definition of generative UI, right? It's
[03:32] allowing agents to play a role in
[03:35] determining what appears on the screen,
[03:36] how information is structured, and in
[03:39] some cases, like in our case, even how
[03:41] the layout is composed. We're giving a
[03:43] lot of control over to the agent versus
[03:46] most agentic applications right now, the
[03:48] agent is just assigning information to
[03:49] display in a preconfigured layout. And
[03:52] so, this takes things to the next level.
[03:54] There's a lot of use cases for this.
[03:56] Even chat applications, think about
[03:58] Slack bots, Discord bots. When we're
[04:00] talking to an agent, a lot of times it's
[04:02] more useful for us to understand what
[04:04] the agent is telling us if we have
[04:06] visuals, not just text responses. So,
[04:08] being able to render components in the
[04:10] middle of a conversation with generative
[04:12] UI and making it custom to our
[04:14] conversation. Now, that is powerful. And
[04:16] then we have the idea of co-creator
[04:18] workspaces. This is more like what I
[04:21] built for my use case. And so, this is
[04:23] where you're working with an agent. So,
[04:25] the canvas displays outputs and
[04:28] previews. it becomes this shared working
[04:30] space where our AI generated UI appears
[04:33] and evolves and so dashboards they
[04:35] literally have this as the example and
[04:37] that's exactly what I built. So just
[04:39] trying to get some ideas flowing for you
[04:41] of the kinds of applications you can
[04:43] build with this. I think e-commerce
[04:44] stores is another really good example
[04:46] where you have these recommendation
[04:48] algorithms that learn each user and not
[04:50] only is it going to recommend certain
[04:52] products but change the entire layout to
[04:54] focus on what it thinks the user should
[04:56] buy. We're going to see a lot of that in
[04:58] the future. And the other thing that's
[05:00] really important to understand with
[05:01] generative UI is there's actually a
[05:03] spectrum of how much control we're
[05:05] giving to the agent versus the
[05:07] programmer. So, we have three categories
[05:09] here. We got static UI, declarative UI,
[05:12] and open-ended UI. And I know that might
[05:14] sound a little bit like word salad right
[05:16] now, but don't worry, we'll get into
[05:17] this and it's important. And declarative
[05:19] UI, this is what I'm the most interested
[05:21] in. I think this is the most innovative
[05:22] and really what's following Google's A2
[05:24] UI specification where the agent will
[05:27] pick components from a library and then
[05:28] send that off for the front end to
[05:30] display dynamically. So starting with
[05:33] static generative UI, this is the most
[05:35] classic and we see this all the time
[05:37] throughout the web right now. So we're
[05:39] using the agent to really just decide
[05:42] the information to display. So it's not
[05:44] picking the components to render. It's
[05:46] not defining the layout. It's just
[05:47] saying like, okay, this is the
[05:49] temperature in New York City right now.
[05:50] So the agent is fetching this
[05:52] information but it's not deciding
[05:54] anything else in our UI. Then on the
[05:56] complete opposite end of the spectrum we
[05:59] have open-ended generative UI. And this
[06:01] is where the agent decides not just the
[06:03] components and layouts but it literally
[06:05] generates all of the code for the HTML,
[06:08] CSS, JSX, whatever on the fly to render
[06:11] in the front end. And so it is the most
[06:13] flexible. But obviously security and
[06:16] performance are a big concern here
[06:18] because really we're just rendering
[06:19] completely arbitrary content. So I don't
[06:22] know about you, but I wouldn't be very
[06:24] comfortable with my agent generating the
[06:27] entire UI on the fly for my users in an
[06:30] application. And so that's what leads us
[06:32] to the option in the middle, declarative
[06:35] generative UI. And so this is what I'm
[06:37] very interested in. It's the idea of we
[06:39] have a preconfigured library of
[06:42] components that the agent can choose
[06:44] from. So it can say I want this one,
[06:45] this one, this one. Let's put it in this
[06:47] layout and then here are the parameters.
[06:49] This is the exact data, the numbers and
[06:51] text to display. And so it still has a
[06:54] lot of freedom around what kind of
[06:57] interface we generate, but it's going to
[06:58] be within bounds that we get to control
[07:01] through the component library and the
[07:02] prompting for our agent. And I will say
[07:05] there are definitely pros and cons to
[07:07] these different kinds of generative UI.
[07:09] And so that's why it's important for us
[07:10] to choose a tech stack that is Gen UI
[07:13] agnostic. That's a tongue twister for me
[07:15] for some reason. But yeah, we have AGUI
[07:18] as our protocol. Like I said, for
[07:19] connecting our agents to our front end,
[07:21] it's going to work no matter if it is
[07:22] static, open-ended, or declarative
[07:24] GenUI. And then Copilot Kit as our
[07:27] front-end framework to render everything
[07:29] and work with our agent. This is also
[07:31] going to work no matter what. And so the
[07:33] use case that I'm showing you and what
[07:35] I'm most interested in is that in the
[07:36] middle we're picking from a component
[07:38] library, but we really can build any
[07:41] kind of application with this text
[07:42] stack. All right. So now that you know
[07:44] how generative UI works at a high level,
[07:46] I want to get more into my use case and
[07:48] really explain the text stack to you and
[07:51] how each layer communicates with each
[07:53] other because this will really drive
[07:54] home exactly how generative UI works.
[07:57] And then I promise I won't get too in
[07:59] the weeds, but I want to show you the
[08:00] code at least a little bit to help you
[08:02] understand how our agent has this
[08:04] component library to pick from and how
[08:06] we have this contract with the front
[08:08] end. So it knows what kind of components
[08:11] can it expect and exactly how does it
[08:13] render those. And so the first thing
[08:16] here of course is we have our input.
[08:18] This is the AI research that we've done
[08:20] with an agent that we want to extract
[08:22] the insights and the TLDDR from. And so
[08:25] I'll show you an example really quick
[08:26] here. So this is the homepage for my
[08:28] second brain research dashboard. I of
[08:31] course have been following along with
[08:32] all the developments with OpenClaw,
[08:34] otherwise known or previously known as
[08:36] Claudebot. And so I've been doing a lot
[08:38] of research with agents. This is one
[08:40] example of a markdown document that I
[08:42] had. And so I can just go ahead and send
[08:44] this in. Boom. There is the input. And
[08:46] now we instantly have the process
[08:48] triggered here where there's an agent
[08:50] working behind the scenes right now
[08:51] selecting the components and the layout.
[08:53] And take a look at that. Now we're 40%
[08:55] complete because it has classified the
[08:58] document. And so this is really how
[08:59] we're defining the layout. And now after
[09:02] that, it's going to select the
[09:03] individual components from the library.
[09:06] And so going back to our diagram here,
[09:08] we'll let this keep generating behind
[09:10] the scenes. The reason I care about this
[09:12] use case in the first place is because
[09:14] I've really been suffering from I'll
[09:16] call it markdown fatigue recently. I
[09:18] know it's a really silly thing, but as
[09:19] I'm using my second brain doing a lot of
[09:21] research with my agents, there's just
[09:23] always these walls of text that I have
[09:25] to parse through. As much as I try to
[09:27] keep my agents concise in their
[09:29] generations, I've just gotten so sick of
[09:31] reading through Markdown. That's what
[09:33] actually inspired me to build out this
[09:35] use case so I have these dashboards to
[09:37] extract insights a lot faster. And so,
[09:39] generative UI solves the problem here
[09:42] because it also adapts the content to
[09:44] what I need to know. And then if I ever
[09:46] think that the dashboard doesn't give me
[09:48] what I think I should know, then I just
[09:49] have to adjust the prompt for the agent.
[09:51] So it's really really flexible and I can
[09:53] evolve the system over time. It's just
[09:55] like the principles that I teach for
[09:57] agentic coding. And so we have our
[09:59] podantic agent in the back end. It takes
[10:01] this input and it defines the layout and
[10:03] the components just like we saw it
[10:05] starting to do in our browser. And so
[10:08] whenever it decides to generate a
[10:10] component, it's going to output a
[10:12] specific JSON. This is following the A2
[10:14] UI protocol. And so I've talked about
[10:17] this a little bit already, but
[10:19] essentially it defines like, okay,
[10:20] here's the ID for the component. Here is
[10:22] the name of the component. So the front
[10:24] end knows what to render. And then we
[10:26] have the children. So that helps define
[10:27] the layout as well. And then another
[10:29] thing that I'm not showing here is the
[10:31] props. And so for any component that we
[10:33] have in the front end, there's certain
[10:34] text numbers that we have to display. So
[10:37] the agent is deciding those as well,
[10:39] just like it would with static
[10:41] generative UI. And so the agent is going
[10:43] to come up with a bunch of these JSON
[10:46] configurations, all the components that
[10:47] it wants to send in, and then we're
[10:49] going to be streaming that to our front
[10:51] end through AGUI. So what we have here
[10:54] is a standard for events that the agent
[10:56] is going to emit to keep this real-time
[10:59] sync between our backend and our front
[11:01] end. And we saw that just now in the
[11:03] dashboard, the percentage went from zero
[11:05] to 40%, because the agent said, "Hey,
[11:07] I've started my run. I'm beginning to
[11:09] generate the dashboard." So we display
[11:10] that in our front end. And then it
[11:12] decides the layout and it moves on to
[11:14] generating the components. And so we
[11:15] update the progress in the front end.
[11:17] And I'm not doing it here, but we could
[11:19] also theoretically stream these
[11:21] components. So we watch the dashboard
[11:23] being built in real time. In my case,
[11:25] I'm just waiting for everything and
[11:26] displaying it all at once, but that
[11:28] would be possible as well. We have this
[11:30] really dynamic sync thanks to AGUI. And
[11:32] then of course, Copilot Kit makes that
[11:34] really easy to render everything. And it
[11:35] has that direct integration with AGUI
[11:38] and Pideantic AI as well. And so all
[11:41] this together just makes this really
[11:42] seamless experience of being able to
[11:44] have the front end connected directly to
[11:46] the agent. And this would be hundreds or
[11:49] even thousands of lines of code if I
[11:52] wasn't using Copilot Kit, AGUI, and
[11:55] Pideantic AI. And going into the code
[11:57] just a little bit here. I promise I'll
[11:59] stay high level. I just want to show you
[12:01] how we have this sort of contract
[12:03] between the backend and the front end.
[12:05] So we're giving the agent options. here
[12:07] are all of the different components that
[12:09] you can render. And so, as a part of our
[12:12] system prompt to the agent, we're
[12:13] describing when we wanted to use these
[12:15] different components and exactly how to
[12:17] define things like the props, what are
[12:19] the the text and numbers that you want
[12:21] to display in each component. And so,
[12:24] telling it what it has access to plus
[12:26] the system prompt is how we're guiding
[12:28] the agent for generating these
[12:30] components. And as a part of the system
[12:31] prompt, we're also describing to it the
[12:34] A2 UI specification. This is exactly how
[12:36] you output a component with the name,
[12:39] the props, the ID, that kind of thing.
[12:41] And then we have the same sort of
[12:43] contract in the front end. And so all of
[12:45] the same components are called out here,
[12:47] but in the front end, we have the actual
[12:49] JSX that we're going to render when the
[12:51] agent chooses that component as well as
[12:53] the props for the data that it wants to
[12:56] display. And so for every single one of
[12:57] the components here, I have it defined
[12:59] in this AGUI folder, just keeping it
[13:01] really nice and organized. And I won't
[13:03] show you all of these obviously, but I
[13:05] do have one of them right here. And just
[13:07] to show you how simple it is, it really
[13:09] is just a basic React component, but
[13:12] it's the agent that decides when we
[13:13] render this. And it decides all the
[13:15] values. Like for this table component,
[13:17] it decides here's the headers, here's
[13:19] the rows, this is the title and the the
[13:21] subtitle. And it's even optional. Like
[13:23] it decides all of that. It's the front
[13:25] end's job to receive the layout and the
[13:28] component requests and then map that to
[13:30] all these components that is going to
[13:32] generate. And it's not like we
[13:34] absolutely need Pantank AI or Copilot
[13:37] Kit to do this. I could use a different
[13:38] agent framework. You don't even really
[13:40] need to use AGUI. I don't need C-Pilot
[13:43] kit. I could even use a different
[13:44] specification besides A2UI. But man,
[13:47] does this text stack together just make
[13:49] it so easy for me to build these
[13:51] applications. I've been working on some
[13:53] other proof of concepts, building out
[13:54] this one in particular. It has been a
[13:57] blast and it just works so incredibly
[13:59] well. And so I know there's quite a few
[14:01] things that we got going on here, but
[14:02] together it makes these really powerful
[14:04] applications that and I really just do
[14:07] see this as the future of software. So
[14:09] let's actually go back to our dashboard
[14:10] here. So this is what we saw the start
[14:12] of the generation and now here we go.
[14:14] This is generated dynamically for us. We
[14:16] saw this appear in real time. And I know
[14:18] that like spacing and things is not
[14:20] perfect. This is more of just a
[14:23] demonstration for you. But I'm still
[14:25] just blown away by the kinds of things
[14:26] that we're able to generate here. It
[14:28] looks so so good. And by the way, this
[14:31] has actually helped me quite a bit with
[14:32] my research on on Claudebot or I guess I
[14:35] should say OpenClaw. And then also this
[14:37] alternative called Nano Claw, which I
[14:39] might cover in a video on my channel
[14:41] soon. So that's another really
[14:42] interesting alternative to OpenClaw. But
[14:46] anyway, I digress. you can see how easy
[14:47] it is to get sucked into the research
[14:49] you're doing with your agents. But for
[14:51] this video here, I really hope that you
[14:53] found it helpful with generative UI,
[14:55] understanding how it works, why it's so
[14:57] powerful, how you can build with it
[14:59] yourself. And I really do encourage you
[15:01] to take the template that I have linked
[15:02] in description and check it out
[15:04] yourself. And I will be doing more
[15:06] content on generative UI. And so if
[15:08] you're looking forward to that or just
[15:09] more content on building agents in
[15:11] general, I would really appreciate a
[15:13] like and a subscribe. And with that, I
[15:15] will see you in the next


## Video Metadata

- **Channel**: [Cole Medin](https://www.youtube.com/@ColeMedin)
- **Duration**: 15 minutes 18 seconds
- **Published**: Video extracted on 2026-02-09
- **Video ID**: MD8VQzvMVek
- **Source**: [YouTube](https://www.youtube.com/watch?v=MD8VQzvMVek)