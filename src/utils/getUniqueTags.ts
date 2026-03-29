import { slugifyStr } from "./slugify";

const getUniqueTags = (posts: any[]) => {
  let tags: string[] = [];
  const filteredPosts = posts.filter((post) => !post.draft);
  filteredPosts.forEach(post => {
    tags = [...tags, ...post.tags]
      .map(tag => slugifyStr(tag))
      .filter(
        (value: string, index: number, self: string[]) =>
          self.indexOf(value) === index
      );
  });
  return tags;
};

export default getUniqueTags;
