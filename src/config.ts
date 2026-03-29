import type { Site, SocialObjects } from "./types";

export const SITE: Site = {
  website: "https://astro-blog-netlify.netlify.app",
  author: "Admin",
  desc: "Personal tech blog covering AI, automation, and self-hosting.",
  title: "AImplifi Blog",
  ogImage: "astropaper-og.jpg",
  lightAndDarkMode: true,
  postPerPage: 10,
};

export const LOGO_IMAGE = {
  enable: false,
  svg: true,
  width: 216,
  height: 46,
};

export const SOCIALS: SocialObjects = [
  {
    name: "Github",
    href: "https://github.com/suppg02-sudo",
    linkTitle: `AImplifi on Github`,
    active: true,
  },
  {
    name: "Telegram",
    href: "https://t.me/your_telegram",
    linkTitle: `Contact via Telegram`,
    active: true,
  },
];
