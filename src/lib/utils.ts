import { getCollection, type CollectionEntry } from "astro:content";
import type { BlogFrontmatter } from "@content/_schemas";

export type { BlogFrontmatter };
export type PostEntry = CollectionEntry<"blog">;

export async function getAllPosts(): Promise<BlogFrontmatter[]> {
  const entries = await getCollection("blog");
  return entries
    .map((entry) => ({
      ...entry.data,
      postSlug: entry.data.postSlug || entry.id.replace(/\.md$/, ""),
    }))
    .filter((post) => !post.draft)
    .filter((post) => {
      if (!post.series) return true;
      return post.seriesEntry === true;
    })
    .sort(
      (a, b) =>
        Math.floor(new Date(b.pubDatetime).getTime() / 1000) -
        Math.floor(new Date(a.pubDatetime).getTime() / 1000)
    );
}

export async function getPostBySlug(slug: string): Promise<BlogFrontmatter | null> {
  const posts = await getAllPosts();
  return posts.find((p) => p.postSlug === slug) || null;
}

export async function getPostEntry(slug: string): Promise<PostEntry | null> {
  const entries = await getCollection("blog");
  return entries.find((e) => e.data.postSlug === slug || e.id.replace(/\.md$/, "") === slug) || null;
}
