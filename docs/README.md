---
layout: spec
---

# Jekyll + Github Pages 测试

欢迎访问 Jekyll + Github Pages 测试

## Primer-Spec theme 测试

以下是关于 primer-spec theme 的测试情况。

参考 [https://github.com/eecs485staff/primer-spec](https://github.com/eecs485staff/primer-spec)：

- 在 webpage 顶部增加

```markdown
---
layout: spec
---
```

- 在网站 root 目录下增加 `_config.yml`。主要内容如下：

```yml
remote_theme: eecs485staff/primer-spec
plugins:
  - jekyll-remote-theme
  - jekyll-optional-front-matter
  - jekyll-readme-index
  - jekyll-relative-links
  - jemoji
kramdown:
  input: GFM
readme_index:
  remove_originals: true
  with_frontmatter: true
```

<!--  -->
测试 callout。参考文档：[https://eecs485staff.github.io/primer-spec/demo/callouts.html](https://eecs485staff.github.io/primer-spec/demo/callouts.html)

Primer Spec offers five variants of callouts:
- neutral
- info
- warning
- danger
- success

**neutral**
<div class="primer-spec-callout" markdown="1">
  **Pro tip:** Use this to create a simple note box. It's weaker than `info`, but offers stronger emphasis than main body text.
</div>

**info**
<div class="primer-spec-callout info" markdown="1">
  **Pro tip:** Use this for additional information, context or hints.
</div>

**warning**
<div class="primer-spec-callout warning" markdown="1">
  **Pro tip:** Use this to alert readers or when extra care/attention is needed.
</div>

**danger**
<div class="primer-spec-callout danger" markdown="1">
  **Pro tip:** Use this to caution readers about dangerous outcomes (or when something won't work as expected).
</div>

**success**
<div class="primer-spec-callout success" markdown="1">
  **Pro tip:** Use this to celebrate an achievement!
</div>
