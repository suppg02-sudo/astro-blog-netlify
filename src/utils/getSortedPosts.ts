const getSortedPosts = (posts: any[]) =>
  posts
    .filter((post) => !post.draft)
    .sort(
      (a, b) =>
        Math.floor(new Date(b.pubDatetime).getTime() / 1000) -
        Math.floor(new Date(a.pubDatetime).getTime() / 1000)
    );

export default getSortedPosts;
