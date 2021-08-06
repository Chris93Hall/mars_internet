
var qt = {'jQuery': jQuery.noConflict(true)};
qt.jQuery('a').each(function () {qt.jQuery(this).css('background-color', 'yellow')});
qt.jQuery('a').each(function () {qt.jQuery(this).append('(cached)')});

function get_link_urls() {
    var links_list = [];
    qt.jQuery('a').each(function(){links_list.push(this.href)};
    return links_list
}

function gen_random_link_dict(link_list) {
    var link_dict = {}; 
    for (let index=0; index++; index<link_list.length) {
        var cache_status = get_random_cache_status();
        var url = link_list[index];
        link_dict[url] = {'cache_status': cache_status,
                          'cached_until': 'forever',
                          'cached_time': 'null',
                          'queued_time': 'null',
                          'cache_reason': 'autocached'};
    }
    return link_dict; 
}

function get_random_cache_status() {
    var num = Math.random();
    // select betweeen NONE, QUEUED, and CACHED
    if (num < 0.33) {
        return "NONE"
    } else if (num < 0.66) {
        return "QUEUED";
    return "CACHED";
}

function apply_link_annotations(link_dict) {
    qt.jQuery('a').each(function() {
        if (this.href in link_dict) {
            var cache_status = link_list[this.href]['cache_status'];
            var cached_until = link_list[this.href]['cached_until'];
            var cached_time = link_list[this.href]['cached_time'];
            var queued_time = link_list[this.href]['queued_time'];
            var cache_reason = link_list[this.href]['cache_reason'];
            if (cache_status == 'NONE') {
                qt.jQuery(this).css('background-color', 'red')});
                qt.jQuery(this).append('(Unavailable)')});
            } else if (cache_status == 'QUEUED') {
                qt.jQuery(this).css('background-color', 'yellow')});
                qt.jQuery(this).append('(Queued)')});
            } else if (cache_status == 'CACHED') {
                qt.jQuery(this).css('background-color', 'green')});
                qt.jQuery(this).append('(Cached)')});
            }
        }
    })
}
