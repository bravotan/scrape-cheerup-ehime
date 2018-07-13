# Scrape web spiders for Cheerup-ehime

Nan-zo-ko-re?

Scrapy spiders for [cheerup-ehime](https://cheerup-ehime.github.io/)

## Requirements

* Python 3.x
	* Scrapy
	* html2text

## Usage

Run a spider of Uwajima city:

```bash
$ cd scrape-cheerup-ehime
$ scrapy crawl uwajima -s POSTDIR=/path/to/post -s TEMPLATE=/path/to/template.md
(... verbose output ...)
```

