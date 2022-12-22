module.exports = function(eleventyConfig) {

  // Copy `img/` to `_site/img`
  eleventyConfig.addPassthroughCopy("styles");

  eleventyConfig.addPairedShortcode('note', function (content, title) {
    return `
<aside class="site-note site-stack" style="--stack-space: 1rem">
  <h3 >🗒️ ${title}</h3>
  <div class="site-stack">${content}</div>
</aside>`;
  });

};
