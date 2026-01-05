---
layout: spec
---

# Jekyll + Github Pages 测试

欢迎访问 Jekyll + Github Pages 测试

## Primer-Spec theme 测试

以下是关于 primer-spec theme 的测试情况。

### 基本用法

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

### 测试 callout

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

### 测试 Jekyll 定制

`_config.yml` 增加：

```yaml
title: Github Pages + Jekyll Test
description: test Github Pages + Jekyll + Theme
favicon: <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640"><!--!Font Awesome Free v7.1.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2026 Fonticons, Inc.--><path d="M160 144C151.2 144 144 151.2 144 160L144 480C144 488.8 151.2 496 160 496L480 496C488.8 496 496 488.8 496 480L496 160C496 151.2 488.8 144 480 144L160 144zM96 160C96 124.7 124.7 96 160 96L480 96C515.3 96 544 124.7 544 160L544 480C544 515.3 515.3 544 480 544L160 544C124.7 544 96 515.3 96 480L96 160zM224 192C241.7 192 256 206.3 256 224C256 241.7 241.7 256 224 256C206.3 256 192 241.7 192 224C192 206.3 206.3 192 224 192zM360 264C368.5 264 376.4 268.5 380.7 275.8L460.7 411.8C465.1 419.2 465.1 428.4 460.8 435.9C456.5 443.4 448.6 448 440 448L200 448C191.1 448 182.8 443 178.7 435.1C174.6 427.2 175.2 417.6 180.3 410.3L236.3 330.3C240.8 323.9 248.1 320.1 256 320.1C263.9 320.1 271.2 323.9 275.7 330.3L292.9 354.9L339.4 275.9C343.7 268.6 351.6 264.1 360.1 264.1z"/></svg>
```

```yml
title: Github Pages + Jekyll Test
description: test Github Pages + Jekyll + Theme
favicon: /assets/favicon/blog-solid-full.svg
```

### 显示在侧边栏

阿是砥砺奋进啊两地分居阿发

### 不显示在侧边栏
{: .primer-spec-toc-ignore }

阿斯蒂芬开讲啦地方