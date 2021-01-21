BOT_NAME = 'lazarovphoto'
SPIDER_MODULES = ['lazarovphoto.spiders']
NEWSPIDER_MODULE = 'lazarovphoto.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'lazarovphoto.pipelines.DatabasePipeline': 300,
}
