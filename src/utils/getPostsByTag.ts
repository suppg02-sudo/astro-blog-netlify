import { slugifyAll } from "./slugify";

const getPostsByTag = (posts: any[], tag: string) =>
  posts.filter(post => slugifyAll(post.tags).includes(tag));

export default getPostsByTag;
