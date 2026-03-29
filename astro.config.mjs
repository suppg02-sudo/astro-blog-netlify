import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://astro-blog-netlify.netlify.app",
  output: "static",
  integrations: [tailwind(), sitemap()],
  markdown: {
    shikiConfig: {
      theme: "github-dark",
      wrap: true,
    },
  },
  vite: {
    resolve: {
      alias: {
        "@assets": "/src/assets",
        "@components": "/src/components",
        "@layouts": "/src/layouts",
        "@styles": "/src/styles",
        "@utils": "/src/utils",
        "@config": "/src/config.ts",
        "@types": "/src/types.ts",
        "@lib": "/src/lib",
      },
    },
  },
  scopedStyleStrategy: "where",
});
