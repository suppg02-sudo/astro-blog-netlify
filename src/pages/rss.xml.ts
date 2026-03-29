import rss from "@astrojs/rss";
import { SITE } from "@config";
import { getAllPosts } from "@lib/utils";

export async function GET() {
  const posts = await getAllPosts();

  return rss({
    title: SITE.title,
    description: SITE.desc,
    site: SITE.website,
    items: posts.map((data) => ({
      link: `posts/${data.postSlug}`,
      title: data.title,
      description: data.description,
      pubDate: new Date(data.pubDatetime),
    })),
  });
}
