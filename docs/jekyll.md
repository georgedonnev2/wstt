---
layout: spec
---

# Jekyll 本地测试

想到能否用 docker 运行 Jekyll。因为以前尝试 Jekyll 本地预览时，要装这装那。尤其是 Ruby 版本和 macOS 自带的 Ruby 还不一样，安装过程很折腾。咨询大模型后可行，就开始测试！

## 添加国内仓库源

参考资料增加了国内仓库源。添加完成后的配置文件如下：

```yaml
{
  "builder": {
    "gc": {
      "defaultKeepStorage": "20GB",
      "enabled": true
    }
  },
  "experimental": false,
  "registry-mirrors": [
    "https://docker.1ms.run",
    "https://docker.m.daocloud.io",
    "https://docker.1panel.live",
    "https://dockerproxy.net",
    "https://docker.xuanyuan.me",
    "https://docker-0.unsee.tech",
    "https://registry.cyou"
  ]
}
```

## 拉取镜像

咨询大模型后，得到拉取镜像命令如下：
```bash
docker pull jekyll/jekyll:latest
```

拉取完成后查看镜像：
```bash
~ % docker image ls
REPOSITORY      TAG       IMAGE ID       CREATED         SIZE
jekyll/jekyll   latest    3c7afda80cab   3 years ago     829MB
```

## 运行容器

执行命令启动容器：
```bash
docker run -it -v ~/gdweb/log:/srv/jekyll -p 4000:4000 jekyll/jekyll jekyll serve
```

报错如下：
```bash
docker run -it -v ~/gdweb/log:/srv/jekyll -p 4000:4000 jekyll/jekyll jekyll serve
ruby 3.1.1p18 (2022-02-18 revision 53f5fc4236) [x86_64-linux-musl]
Configuration file: none
            Source: /srv/jekyll
       Destination: /srv/jekyll/_site
 Incremental build: disabled. Enable with --incremental
      Generating... 
                    done in 0.036 seconds.
 Auto-regeneration: enabled for '/srv/jekyll'
                    ------------------------------------------------
      Jekyll 4.2.2   Please append `--trace` to the `serve` command 
                     for any additional information or backtrace. 
                    ------------------------------------------------
<internal:/usr/local/lib/ruby/site_ruby/3.1.0/rubygems/core_ext/kernel_require.rb>:85:in `require': cannot load such file -- webrick (LoadError)
	from <internal:/usr/local/lib/ruby/site_ruby/3.1.0/rubygems/core_ext/kernel_require.rb>:85:in `require'
	from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/commands/serve/servlet.rb:3:in `<top (required)>'
	from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/commands/serve.rb:179:in `require_relative'
	from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/commands/serve.rb:179:in `setup'
	from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/commands/serve.rb:100:in `process'
	from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/command.rb:91:in `block in process_with_graceful_fail'
	from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/command.rb:91:in `each'
	from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/command.rb:91:in `process_with_graceful_fail'
	from /usr/gem/gems/jekyll-4.2.2/lib/jekyll/commands/serve.rb:86:in `block (2 levels) in init_with_program'
	from /usr/gem/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `block in execute'
	from /usr/gem/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `each'
	from /usr/gem/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `execute'
	from /usr/gem/gems/mercenary-0.4.0/lib/mercenary/program.rb:44:in `go'
	from /usr/gem/gems/mercenary-0.4.0/lib/mercenary.rb:21:in `program'
	from /usr/gem/gems/jekyll-4.2.2/exe/jekyll:15:in `<top (required)>'
	from /usr/gem/bin/jekyll:25:in `load'
	from /usr/gem/bin/jekyll:25:in `<main>'
```

咨询大模型后得到如下方案。依次执行就可以了。其中
```bash
cd ~/gdweb/log

# 创建新的 Jekyll 站点
docker run --rm -it -v $(pwd):/srv/jekyll jekyll/jekyll jekyll new . --force


# 安装 webrick
docker run --rm -it -v $(pwd):/srv/jekyll jekyll/jekyll bundle add webrick

# 启动服务
docker run --rm -v $(pwd):/srv/jekyll -p 4000:4000 jekyll/jekyll jekyll serve
```

其中，第1个命令“创建新的 Jekyll站点”，运行后没有退出，按 `ctrl`+`c` 后退出。

3个命令依次执行后，在本地浏览器输入 `localhost:4000` 就可以看到网页了。


## 参考资料

- [2026最新零基础安装，10分钟学会跑本地AI/n8n/Ollama | Docker Desktop 保姆级教学 | 附汉化+国内镜像源](https://www.bilibili.com/video/BV1q7i9BTE4N)，B站，小in分享，2026-01-09

