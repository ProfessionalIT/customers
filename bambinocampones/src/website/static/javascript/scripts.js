window.onerror = function(desc, page, line, chr) {
    /* alert('JavaScript error occurred! \n'
     +'\nError description: \t'+desc
     +'\nPage address:      \t'+page
     +'\nLine number:       \t'+line
     );*/
}
jQuery(function() {
    jQuery('a').focus(function() {
        this.blur();
    });
    SI.Files.stylizeAll();
    slider.init();
    mc.init();

    jQuery('input.text-default').each(function() {
        jQuery(this).attr('default', jQuery(this).val());
    }).focus(function() {
        if (jQuery(this).val() == jQuery(this).attr('default'))
            jQuery(this).val('');
    }).blur(function() {
        if (jQuery(this).val() == '')
            jQuery(this).val(jQuery(this).attr('default'));
    });

    jQuery('input.text,textarea.text').focus(function() {
        jQuery(this).addClass('textfocus');
    }).blur(function() {
        jQuery(this).removeClass('textfocus');
    });

    var popopenobj = 0, popopenaobj = null;
    jQuery('a.popup').click(function() {
        var pid = jQuery(this).attr('rel').split('|')[0], _os = parseInt(jQuery(this).attr('rel').split('|')[1]);
        var pobj = jQuery('#' + pid);
        if (!pobj.length)
            return false;
        if ( typeof popopenobj == 'object' && popopenobj.attr('id') != pid) {
            popopenobj.hide(50);
            jQuery(popopenaobj).parent().removeClass(popopenobj.attr('id').split('-')[1] + '-open');
            popopenobj = null;
        }

        if (pobj.is(':hidden')) {
            var _o = jQuery(this).offset();
            //var _l=parseInt(_o.left)-parseInt(_os)+parseInt(jQuery(this).width())/2;
            var _l = (jQuery('.wrap', '#top').offset().left + jQuery('.wrap', '#top').width()) - pobj.width();
            var _t = parseInt(_o.top) + parseInt(jQuery(this).height()) + 5;
            pobj.css({
                left : _l,
                top : _t
            }).slideDown(function() {
                jQuery('div.close a', pobj).click(function() {
                    pobj.slideUp();
                    jQuery(popopenaobj).parent().removeClass(pobj.attr('id').split('-')[1] + '-open');
                    popopenobj = 0;
                });
                var fobj = jQuery('form input.text:first', pobj);
                if (fobj.length)
                    fobj.get(0).focus();
            });
            jQuery(this).parent().addClass(pid.split('-')[1] + '-open');
            popopenobj = pobj;
            popopenaobj = this;
        } else {
            pobj.slideUp();
            jQuery(this).parent().removeClass(pid.split('-')[1] + '-open');
            popopenobj = 0;
        }
        return false;
    });

    jQuery('p.images img').click(function() {
        var newbg = jQuery(this).attr('src').split('bg/bg')[1].split('-thumb')[0];
        jQuery(document.body).css('backgroundImage', 'url(' + _siteRoot + 'images/bg/bg' + newbg + '.jpg)');

        jQuery(this).parent().find('img').removeClass('on');
        jQuery(this).addClass('on');
        return false;
    });

    jQuery('p.colours a').click(function() {
        var sheet = document.createElement('link');
        sheet.setAttribute('rel', 'stylesheet');
        sheet.setAttribute('type', 'text/css');
        sheet.setAttribute('media', 'all');
        sheet.setAttribute('href', _siteRoot + 'css/' + this.id + '/colour.css');

        if (jQuery.browser.safari)
            jQuery('head').append(sheet);
        else
            jQuery(document.body).append(sheet);

        jQuery(this).parent().find('a').removeClass('on');
        jQuery(this).addClass('on');
        return false;
    });

    jQuery('div.bar').slice(1).each(function() {
        jQuery('h2', this).addClass('closed');
        jQuery('div', this).hide();
    });
    jQuery('div.bar h2').click(function() {
        scroll(this, -120);
        jQuery(this).toggleClass('closed').parent().find('div').slideToggle();
    });
    jQuery('#close-tabs').click(function() {
        jQuery('div.bar div:visible').slideUp().parent().find('h2').addClass('closed');
        return false;
    });

    function h42h4(obj, t) {
        var aobjs = jQuery('div.column-right>*'), sel = false;
        var len = aobjs.length;
        for (var i = 0; i < len; i++) {
            if (aobjs[i].tagName.toLowerCase() == 'h4')
                sel = false;
            if (sel)
                switch(t) {
                    case 's' :
                        jQuery(aobjs[i]).show();
                        break;
                    case 'h' :
                        jQuery(aobjs[i]).hide();
                        break;
                    case 't' :
                        jQuery(aobjs[i]).toggle();
                        break;
                    default :
                        jQuery(aobjs[i]).slideToggle(500);
                        break;
                }
            if (aobjs[i] == obj)
                sel = true;
        }
        switch(t) {
            case 's' :
                jQuery(obj).removeClass('closed');
                break;
            case 'h' :
                jQuery(obj).addClass('closed');
                break;
            default :
                jQuery(obj).toggleClass('closed');
                break;
        }
    }

    var h4rp = unescape(get_cookie('id_blog_pref') || '').split(' ');

    jQuery('div.sc-large div.img:has(div.tml)').each(function() {
        jQuery('div.tml', this).hide();
        jQuery(this).append('<a href="#" class="tml_open">&nbsp;</a>').find('a').css({
            left : parseInt(jQuery(this).offset().left) + 864,
            top : parseInt(jQuery(this).offset().top) + 1
        }).click(function() {
            jQuery(this).siblings('div.tml').slideToggle();
            return false;
        }).focus(function() {
            this.blur();
        });
    });
});

// Other functions -->
function scroll(obj, offset) {
    if ( typeof obj.pathname == 'undefined') {
        var jQuerytarget = jQuery(obj);
    } else if (location.pathname.replace(/^\//, '') == obj.pathname.replace(/^\//, '') && location.hostname == obj.hostname) {
        var jQuerytarget = jQuery(obj.hash);
        jQuerytarget = jQuerytarget.length && jQuerytarget || jQuery('[name=' + obj.hash.slice(1) + ']');
    }
    if (jQuerytarget.length) {
        var targetOffset = jQuerytarget.offset().top + offset;
        jQuery('html,body').stop().animate({
            scrollTop : targetOffset
        }, 500, 'swing');
        return false;
    }
}

var slider = {
    num : -1,
    cur : 0,
    cr : [],
    al : null,
    at : 10 * 1000,
    ar : true,
    init : function() {
        if (!slider.data || !slider.data.length)
            return false;
        var d = slider.data;
        slider.num = d.length;
        var pos = Math.floor(Math.random() * 1);
        //slider.num);
        for (var i = 0; i < slider.num; i++) {
            jQuery('#' + d[i].id).css({
                left : ((i - pos) * 1000)
            });
            jQuery('#slide-nav').append('<a id="slide-link-' + i + '" href="#" onclick="slider.slide(' + i + ');return false;" onfocus="this.blur();">' + (i + 1) + '</a>');
        }

        jQuery('img,div#slide-controls', jQuery('div#slide-holder')).fadeIn();
        slider.text(d[pos]);
        slider.on(pos);
        slider.cur = pos;
        window.setTimeout('slider.auto();', slider.at);
    },
    auto : function() {
        if (!slider.ar)
            return false;

        var next = slider.cur + 1;
        if (next >= slider.num)
            next = 0;
        slider.slide(next);
    },
    slide : function(pos) {
        if (pos < 0 || pos >= slider.num || pos == slider.cur)
            return;

        window.clearTimeout(slider.al);
        slider.al = window.setTimeout('slider.auto();', slider.at);

        var d = slider.data;
        for (var i = 0; i < slider.num; i++)
            jQuery('#' + d[i].id).stop().animate({
                left : ((i - pos) * 1000)
            }, 1000, 'swing');

        slider.on(pos);
        slider.text(d[pos]);
        slider.cur = pos;
    },
    on : function(pos) {
        jQuery('#slide-nav a').removeClass('on');
        jQuery('#slide-nav a#slide-link-' + pos).addClass('on');
    },
    text : function(di) {
        slider.cr['a'] = di.client;
        slider.cr['b'] = di.desc;
        slider.ticker('#slide-client span', di.client, 0, 'a');
        slider.ticker('#slide-desc', di.desc, 0, 'b');
    },
    ticker : function(el, text, pos, unique) {
        if (slider.cr[unique] != text)
            return false;

        ctext = text.substring(0, pos) + (pos % 2 ? '-' : '_');
        jQuery(el).html(ctext);

        if (pos == text.length)
            jQuery(el).html(text);
        else
            window.setTimeout('slider.ticker("' + el + '","' + text + '",' + (pos + 1) + ',"' + unique + '");', 30);
    }
};

var mc = {
    flag : 0,
    auto_open : true,
    auto_play : true,
    pulse_go : false,
    hov_html : '<div id="mcdivhover"></div>',
    init : function() {
        if (!jQuery('#media-centre').length)
            return;

        if (mc.auto_open && !get_cookie('id_visited')) {
            jQuery(window).load(function() {
                setTimeout(function() {
                    mc.toggle(0);
                }, 500);
            });
        }
        set_cookie('id_visited', 'true', 365, 'index.html');
        if (!get_cookie('id_pclicked')) {
            mc.pulse_go = true;
            mc.pulse(1);
        }
        jQuery('#media-centre').css({
            top : -419
        });
        jQuery('#media-centre-holder').css({
            height : 0
        }).show();
        jQuery('#media-centre-tabs a:first').addClass('on');
        jQuery('#' + jQuery('#media-centre-tabs a:first').attr('rel')).show();

        jQuery('#media-centre-tabs a').click(function() {
            jQuery('#media-centre-tabs a').removeClass('on');
            jQuery(this).addClass('on');

            jQuery('div#media-centre-videos div').hide();
            jQuery('#' + jQuery(this).attr('rel')).show();
        });

        jQuery('div#media-centre-videos div p.video').hover(function() {
            jQuery(this).append(mc.hov_html);
            var o = jQuery(this).find('img').offset();
            jQuery('#mcdivhover').show();
        }, function() {
            jQuery('#mcdivhover').remove();
        }).click(function() {
            jQuery('div#media-centre-videos div p.video').removeClass('playing');
            jQuery(this).addClass('playing');
            mc.play(jQuery(this).find('span.file').html());
            if (jQuery(this).is('.ontwerp'))
                jQuery('#ontwerp-tag').fadeIn();
            else
                jQuery('#ontwerp-tag').fadeOut();
        });

        jQuery('div#media-centre-videos div p.news').hover(function() {
            jQuery(this).addClass('hover');
        }, function() {
            jQuery(this).removeClass('hover');
        }).click(function() {
            location.href = jQuery(this).find('span.url').html();
        });
    },
    toggle : function(pulse_set) {
        if (mc.flag)
            mc.pause();
        if (pulse_set && !get_cookie('id_pclicked')) {
            mc.pulse_go = false;
            set_cookie('id_pclicked', 'true', 365, 'index.html');
        }
        jQuery('.mca').toggleClass('t');

        jQuery('#media-centre-holder').stop().animate({
            height : mc.flag ? 0 : 419
        }, 1000, 'swing');
        jQuery('#media-centre').stop().animate({
            top : mc.flag ? -419 : 0
        }, 1000, 'swing', function() {
            try {
                if (mc.flag && mc.auto_play) {
                    var f = jQuery('div#media-centre-videos div p.video:first');
                    jQuery('div#media-centre-videos div p.video').removeClass('playing');
                    f.addClass('playing');
                    mc.play(jQuery(this).find('span.file').html());
                    if (f.is('.ontwerp'))
                        jQuery('#ontwerp-tag').fadeIn();
                    else
                        jQuery('#ontwerp-tag').fadeOut();
                    mc.auto_play = false;
                }
            } catch(e) {
            }
        });
        if (jQuery('#pusher').length) {
            jQuery('.tml_open').hide();
            jQuery('#pusher div').stop().animate({
                height : mc.flag ? 0 : 419
            }, 1000, 'swing', function() {
                jQuery('.tml_open').each(function() {
                    jQuery(this).show().css({
                        top : jQuery(this).offset().top + ((mc.flag ? 1 : -1) * 120)
                    });
                });
            });
        }
        set_cookie('id_mc', mc.flag ? 'closed' : 'open', 30, 'index.html');
        mc.flag = !mc.flag;
    },
    play : function(src) {
        if (!document.getElementById || !document.getElementById('objectmc'))
            return false;
        document.getElementById('objectmc').playVideo(_siteRoot + src);
    },
    pause : function() {
        if (!document.getElementById || !document.getElementById('objectmc'))
            return false;
        document.getElementById('objectmc').pauseVideo();
    },
    pulse : function(s) {
        if (!mc.pulse_go)
            jQuery('#mc-pulse').fadeOut(750);
        else if (s)
            jQuery('#mc-pulse').fadeIn(750, function() {
                mc.pulse(0);
            });
        else
            jQuery('#mc-pulse').fadeOut(750, function() {
                mc.pulse(1);
            });
    },
    checkHash : function() {
        if (!document.getElementById || !document.getElementById('objectvp'))
            return false;
        var id = location.hash.replace(/[^0-9]/, '');
        if (id != '') {
            setTimeout(function() {
                document.getElementById('objectvp').moveId(id);
                load_comments(id);
            }, 750);
        }
    },
    live : function() {
        mc.toggle(0);
        if (mc.flag) {
            window.setTimeout(function() {
                mc.play(jQuery('p.video:first').attr('rel'));
            }, 1100);
            window.setTimeout('mc.live();', 42 * 1000);
        } else
            window.setTimeout('mc.live();', 2.5 * 60 * 1000);
    }
};

var cmap = {
    is_open : false,
    gmap : false,
    form_id : 'contact-form',
    map_id : 'contact-map',
    time : 750,
    open : function() {
        if (cmap.is_open)
            return false;
        jQuery('#' + cmap.form_id).fadeOut(cmap.time, function() {
            jQuery('#' + cmap.map_id).fadeIn(cmap.time, function() {
                if (GBrowserIsCompatible() && !cmap.gmap) {
                    cmap.gmap = true;
                    var map = new GMap2(document.getElementById('gmap'));
                    var ll = new GLatLng(51.465772, -0.298347);
                    map.setCenter(ll, 13);
                    map.addOverlay(new GMarker(ll));
                    map.addControl(new GSmallMapControl());
                    map.addControl(new GMapTypeControl());
                    cmap.gdir = new GDirections(map, document.getElementById('cmap_dir'));
                    GEvent.addListener(cmap.gdir, 'error', cmap.handleErrors);
                }
            });
        });
        cmap.is_open = true;
    },
    close : function() {
        if (!cmap.is_open)
            return false;
        jQuery('#' + cmap.map_id).fadeOut(cmap.time, function() {
            jQuery('#' + cmap.form_id).fadeIn(cmap.time);
        });
        cmap.is_open = false;
    },
    directions : function(to) {
        cmap.gdir.load('from: Kew Road, Richmond, UK to: ' + to, {
            'locale' : 'en_UK'
        });
    },
    handleErrors : function() {
        if (cmap.gdir.getStatus().code == G_GEO_UNKNOWN_ADDRESS)
            alert("No corresponding geographic location could be found for one of the specified addresses. This may be due to the fact that the address is relatively new, or it may be incorrect.\nError code: " + cmap.gdir.getStatus().code);
        else if (cmap.gdir.getStatus().code == G_GEO_SERVER_ERROR)
            alert("A geocoding or directions request could not be successfully processed, yet the exact reason for the failure is not known.\n Error code: " + cmap.gdir.getStatus().code);
        else if (cmap.gdir.getStatus().code == G_GEO_MISSING_QUERY)
            alert("The HTTP q parameter was either missing or had no value. For geocoder requests, this means that an empty address was specified as input. For directions requests, this means that no query was specified in the input.\n Error code: " + cmap.gdir.getStatus().code);
        else if (cmap.gdir.getStatus().code == G_GEO_BAD_KEY)
            alert("The given key is either invalid or does not match the domain for which it was given. \n Error code: " + cmap.gdir.getStatus().code);
        else if (cmap.gdir.getStatus().code == G_GEO_BAD_REQUEST)
            alert("A directions request could not be successfully parsed.\n Error code: " + cmap.gdir.getStatus().code);
        else
            alert("An unknown error occurred.");
    }
};

function toolbox_save() {
    if (jQuery('#popup-toolbox').length) {
        var bg = jQuery('#popup-toolbox img.on').attr('src').split('bg/bg')[1].split('-thumb')[0];
        var colour = jQuery('#popup-toolbox a.on').attr('id');

        if (jQuery('#toolbox-remember').is(':checked')) {
            jQuery.get(_root, {
                set_bg : bg,
                set_colour : colour
            }, function() {
            });
        }
        jQuery('#popup-toolbox').fadeOut();
        jQuery('li.toolbox').removeClass('toolbox-open');
    }
}

var client_root = _root + 'client/';
function client_login(form) {
    jQuery.post(client_root, {
        user : form.client_user.value,
        pass : form.client_pass.value
    }, function(data) {
        if (data == '0')
            jQuery('#popup-client p.error').fadeIn();
        else
            location.href = client_root;
    });
}

function cms_login(form) {
    jQuery.post(_siteRoot + 'ajax-login.php', {
        user : form.cms_user.value,
        pass : form.cms_pass.value
    }, function(data) {
        if (data == '0')
            jQuery('#popup-cms p.error').fadeIn();
        else
            location.href = _root + 'wp-admin/';
    });
}

Array.prototype.in_array = function(v) {
    for (var i in this)
    if (this[i] == v)
        return true;
    return false;
}
Array.prototype.remove = function(s) {
    for ( i = 0; i < this.length; i++)
        if (s == this[i])
            this.splice(i, 1);
}
var star_off = _siteRoot + 'images/star-off.png', star_on = _siteRoot + 'images/star-on.png', star_html = '<p class="stars" rel="%s%">';
for (var i = 1; i < 6; i++)
    star_html += '<img src="' + star_off + '" alt="" id="star_%s%_' + i + '" onmouseover="feedback_stars(this,\'over\',\'%s%\',' + i + ');" onmouseout="feedback_stars(this,\'out\',\'%s%\',' + i + ');" onclick="feedback_stars(this,\'click\',\'%s%\',' + i + ');" width="15" height="15" />';
star_html += '<input type="hidden" id="rating_%s%" name="rating_%s%" value="-1" /></p>';

var fb_html = '<div id="feedback_div"><form action="' + _siteRoot + 'feedback.php" method="post"><a href="#" id="fb_close" onclick="feedback_close();return false;" onfocus="blur();">Close</a>' + '<div class="rate"><p>This page</p><p class="indent">Design:</p>' + star_html.replace(/%s%/gi, 'page_design') + '<p class="indent">Content:</p>' + star_html.replace(/%s%/gi, 'page_content') + '<p class="indent">Ease of use:</p>' + star_html.replace(/%s%/gi, 'page_ease') + '<p class="indent">Overall:</p>' + star_html.replace(/%s%/gi, 'page_overall') + '</div>' + '<div class="rate"><p>Whole site</p><p class="indent">Design:</p>' + star_html.replace(/%s%/gi, 'site_design') + '<p class="indent">Content:</p>' + star_html.replace(/%s%/gi, 'site_content') + '<p class="indent">Ease of use:</p>' + star_html.replace(/%s%/gi, 'site_ease') + '<p class="indent">Overall:</p>' + star_html.replace(/%s%/gi, 'site_overall') + '</div>' + '<div class="form"><label>Name: <input type="text" name="name" value="" class="text" /></label><label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Email: <input type="text" name="email" value="" class="text" /></label><label class="ta">Comments:<br /><textarea name="comments" cols="10" rows="5"></textarea></label><br style="clear:both;" /><input type="submit" name="submit" class="button" value="" /></div>' + '</form></div>';

function feedback(obj) {
    if (fb_html != '') {
        jQuery(document.body).append(fb_html);
        fb_html = '';
        _offset = jQuery(obj).offset();
        jQuery('#feedback_div').css({
            'left' : _offset.left - jQuery('#feedback_div').width() + jQuery(obj).width() - 30,
            'top' : _offset.top - 240
        });
    }
    if (jQuery('#feedback_div').is(':visible'))
        jQuery('#feedback_div').fadeOut(250);
    else
        jQuery('#feedback_div').fadeIn(250);
}

function feedback_close() {
    if (jQuery('#feedback_div').is(':visible'))
        jQuery('#feedback_div').fadeOut(250);
}


jQuery(document).click(function(e) {
    if (jQuery('#feedback_div').is(':visible')) {
        var obj = e.target, ids = [];
        while (obj.parentNode) {
            ids[ids.length] = obj.id;
            obj = obj.parentNode;
        }
        if (!ids.in_array('feedback_div') && !ids.in_array('feedback_a'))
            jQuery('#feedback_div').fadeOut(250);
    }
});
var fb_r = [];
function feedback_stars(obj, b, s, r) {
    switch(b) {
        case 'over' :
            for (var i = 1; i < 6; i++) {
                if (i <= r)
                    jQuery('#star_' + s + '_' + i).attr('src', star_on);
                else
                    jQuery('#star_' + s + '_' + i).attr('src', star_off);
            }
            break;
        case 'out' :
            for (var i = 1; i < 6; i++) {
                if ( typeof fb_r[s] != 'undefined' && i <= fb_r[s])
                    jQuery('#star_' + s + '_' + i).attr('src', star_on);
                else
                    jQuery('#star_' + s + '_' + i).attr('src', star_off);
            }
            break;
        case 'click' :
            fb_r[s] = r;
            jQuery('#rating_' + s).val(r);
            break;
    }
}

function load_comments(id) {
    jQuery('#comment_post_ID').val(id);
    jQuery('#video-comments').html('<p>Loading comments&hellip;</p>');

    jQuery.getJSON(_siteRoot + 'json-comments.php?id=' + id, function(data) {
        var html = '';
        jQuery('#video-comments').html('<p>There are no comments for this video.</p>');
        jQuery.each(data, function() {
            html += '<div class="comment"><p class="author colour">' + this.comment_author + ' says:</p><p class="date">' + this.date + '</p><p class="message">' + this.comment_content + '</p></div>';
            html += '<div class="hr"></div>';
        });
        if (html != '')
            jQuery('#video-comments').html(html);
    });
}

// STYLING FILE INPUTS 1.0 | Shaun Inman <http://www.shauninman.com/> | 2007-09-07
if (!window.SI) {
    var SI = {};
};
SI.Files = {
    htmlClass : 'SI-FILES-STYLIZED',
    fileClass : 'file',
    wrapClass : 'cabinet',

    fini : false,
    able : false,
    init : function() {
        this.fini = true;

        var ie = 0;
        if (window.opera || (ie && ie < 5.5) || !document.getElementsByTagName) {
            return;
        }
        this.able = true;

        var html = document.getElementsByTagName('html')[0];
        html.className += (html.className != '' ? ' ' : '') + this.htmlClass;
    },
    stylize : function(elem) {
        if (!this.fini) {
            this.init();
        };
        if (!this.able) {
            return;
        };

        elem.parentNode.file = elem;
        elem.parentNode.onmousemove = function(e) {
            if ( typeof e == 'undefined')
                e = window.event;
            if ( typeof e.pageY == 'undefined' && typeof e.clientX == 'number' && document.documentElement) {
                e.pageX = e.clientX + document.documentElement.scrollLeft;
                e.pageY = e.clientY + document.documentElement.scrollTop;
            };
            var ox = oy = 0;
            var elem = this;
            if (elem.offsetParent) {
                ox = elem.offsetLeft;
                oy = elem.offsetTop;
                while ( elem = elem.offsetParent) {
                    ox += elem.offsetLeft;
                    oy += elem.offsetTop;
                };
            };
            var x = e.pageX - ox;
            var y = e.pageY - oy;
            var w = this.file.offsetWidth;
            var h = this.file.offsetHeight;
            this.file.style.top = y - (h / 2) + 'px';
            this.file.style.left = x - (w - 30) + 'px';
        };
    },
    stylizeById : function(id) {
        this.stylize(document.getElementById(id));
    },
    stylizeAll : function() {
        if (!this.fini) {
            this.init();
        };
        if (!this.able) {
            return;
        };

        var inputs = document.getElementsByTagName('input');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type == 'file' && input.className.indexOf(this.fileClass) != -1 && input.parentNode.className.indexOf(this.wrapClass) != -1)
                this.stylize(input);
        };
    }
};

function set_cookie(name, value, expires, path, domain, secure) {
    var today = new Date();
    today.setTime(today.getTime());
    if (expires)
        expires *= (1000 * 60 * 60 * 24);
    var expires_date = new Date(today.getTime() + expires);

    document.cookie = name + '=' + escape(value) + ((expires) ? ';expires=' + expires_date.toGMTString() : '') + ((path) ? ';path=' + path : '') + ((domain) ? ';domain=' + domain : '') + ((secure) ? ';secure' : '');
}

function get_cookie(check_name) {
    var a_all_cookies = document.cookie.split(';');
    var a_temp_cookie = '';
    var cookie_name = '';
    var cookie_value = '';
    var b_cookie_found = false;

    for ( i = 0; i < a_all_cookies.length; i++) {
        a_temp_cookie = a_all_cookies[i].split('=');
        cookie_name = a_temp_cookie[0].replace(/^\s+|\s+jQuery/g, '');

        if (cookie_name == check_name) {
            b_cookie_found = true;
            if (a_temp_cookie.length > 1)
                cookie_value = unescape(a_temp_cookie[1].replace(/^\s+|\s+jQuery/g, ''));
            return cookie_value;
            break;
        }
        a_temp_cookie = null;
        cookie_name = '';
    }
    if (!b_cookie_found)
        return null;
}

function delete_cookie(name, path, domain) {
    if (get_cookie(name))
        document.cookie = name + '=' + ((path) ? ';path=' + path : '') + ((domain) ? ';domain=' + domain : '') + ';expires=Thu,01-Jan-1970 00:00:01 GMT';
}

/**
 * --------------------------------------------------------------------
 * jQuery-Plugin "pngFix"
 * Version: 1.1, 11.09.2007
 * by Andreas Eberhard, andreas.eberhard@gmail.com
 *                      http://jQuery.andreaseberhard.de/
 *
 * Copyright (c) 2007 Andreas Eberhard
 * Licensed under GPL (http://www.opensource.org/licenses/gpl-license.php)
 *
 * Changelog:
 *    11.09.2007 Version 1.1
 *    - removed noConflict
 *    - added png-support for input type=image
 *    - 01.08.2007 CSS background-image support extension added by Scott Jehl, scott@filamentgroup.com, http://www.filamentgroup.com
 *    31.05.2007 initial Version 1.0
 * --------------------------------------------------------------------
 * @example jQuery(function(){jQuery(document).pngFix();});
 * @desc Fixes all PNG's in the document on document.ready
 *
 * jQuery(function(){jQuery(document).pngFix();});
 * @desc Fixes all PNG's in the document on document.ready when using noConflict
 *
 * @example jQuery(function(){jQuery('div.examples').pngFix();});
 * @desc Fixes all PNG's within div with class examples
 *
 * @example jQuery(function(){jQuery('div.examples').pngFix( { blankgif:'ext.gif' } );});
 * @desc Fixes all PNG's within div with class examples, provides blank gif for input with png
 * --------------------------------------------------------------------
 */
(function(jQuery) {
    jQuery.fn.pngFix = function(settings) {
        settings = jQuery.extend({
            blankgif : 'blank.gif'
        }, settings);
        var ie55 = (navigator.appName == 'Microsoft Internet Explorer' && parseInt(navigator.appVersion) == 4 && navigator.appVersion.indexOf('MSIE 5.5') != -1);
        var ie6 = (navigator.appName == 'Microsoft Internet Explorer' && parseInt(navigator.appVersion) == 4 && navigator.appVersion.indexOf('MSIE 6.0') != -1);

        if (jQuery.browser.msie && (ie55 || ie6)) {
            //fix images with png-source
            /*jQuery(this).find("img[@srcjQuery=.png]").each(function() {
            jQuery(this).attr('width',jQuery(this).width());
            jQuery(this).attr('height',jQuery(this).height());
            var prevStyle='';
            var strNewHTML='';
            var imgId=(jQuery(this).attr('id'))?'id="'+jQuery(this).attr('id')+'" ' : '';
            var imgClass=(jQuery(this).attr('class'))?'class="'+jQuery(this).attr('class')+'" ' : '';
            var imgTitle=(jQuery(this).attr('title'))?'title="'+jQuery(this).attr('title')+'" ' : '';
            var imgAlt=(jQuery(this).attr('alt'))?'alt="'+jQuery(this).attr('alt')+'" ' : '';
            var imgAlign=(jQuery(this).attr('align'))?'float:'+jQuery(this).attr('align')+';' : '';
            var imgHand=(jQuery(this).parent().attr('href'))?'cursor:hand;' : '';
            if (this.style.border) {
            prevStyle += 'border:'+this.style.border+';';
            this.style.border='';
            }
            if (this.style.padding) {
            prevStyle += 'padding:'+this.style.padding+';';
            this.style.padding='';
            }
            if (this.style.margin) {
            prevStyle += 'margin:'+this.style.margin+';';
            this.style.margin='';
            }
            var imgStyle=(this.style.cssText);
            strNewHTML += '<span '+imgId+imgClass+imgTitle+imgAlt;
            strNewHTML += 'style="position:relative;white-space:pre-line;display:inline-block;background:transparent;'+imgAlign+imgHand;
            strNewHTML += 'width:'+jQuery(this).width()+'px;'+'height:'+jQuery(this).height()+'px;';
            strNewHTML += 'filter:progid:DXImageTransform.Microsoft.AlphaImageLoader'+'(src=\''+jQuery(this).attr('src')+'\', sizingMethod=\'scale\');';
            strNewHTML += imgStyle+'"></span>';
            if (prevStyle != ''){
            strNewHTML='<span style="position:relative;display:inline-block;'+prevStyle+imgHand+'width:'+jQuery(this).width()+'px;'+'height:'+jQuery(this).height()+'px;'+'">'+strNewHTML+'</span>';
            }
            jQuery(this).hide();
            jQuery(this).after(strNewHTML);
            });*/
            // fix css background pngs
            //jQuery(this).find("*").each(function(){
            jQuery(this).each(function() {
                var bgIMG = jQuery(this).css('background-image');
                if (bgIMG.indexOf(".png") != -1) {
                    var iebg = bgIMG.split('url("')[1].split('")')[0];
                    jQuery(this).css('background-image', 'none');
                    jQuery(this).get(0).runtimeStyle.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(src='" + iebg + "',sizingMethod='" + settings.sizingMethod + "')";
                }
            });
            //fix input with png-source
            /*jQuery(this).find("input[@srcjQuery=.png]").each(function() {
             var bgIMG=jQuery(this).attr('src');
             jQuery(this).get(0).runtimeStyle.filter='progid:DXImageTransform.Microsoft.AlphaImageLoader'+'(src=\''+bgIMG+'\', sizingMethod=\'scale\');';
             jQuery(this).attr('src', settings.blankgif)
             });*/
        }
        return jQuery;
    };
})(jQuery);
jQuery(function() {
    if (jQuery.browser.msie && jQuery.browser.version < 7) {
        // jQuery('div#top h1 a,div#content h2,div.column-third h4,p.date,div#media-centre-tabs a,div.popup').pngFix({sizingMethod:'crop'});
        // jQuery('div#top,div#content div.wrap').pngFix({sizingMethod:'scale'});
    }
});

function get_page_content(slug){
    jQuery.ajax({ 
        type: "POST", 
        url: "/get-content/" + slug, 
        dataType: "json",
        success: function(data) {
            if (data){
                jQuery("title").html(data.titulo);
                jQuery('meta[name=description]').attr('description', data.descricao_completa)
                jQuery('meta[name=keywords]').attr('keywords', data.palavras_chaves);
                obj_return=document.getElementById('conteudo_panel');
                obj_return.innerHTML=data.conteudo;
            }
        }, 
        error: function(e, a) { 
            obj_return=document.getElementById('conteudo_panel');
            obj_return.innerHTML="Failure! " + e + " " + a;
        }
    });
    return false;
}
jQuery(document).ready(function(){
    var loading = jQuery('<img id="loading" alt="Carregando" title="Carregando" src="/static/images/lightbox/images/lightbox-ico-loading.gif" />').appendTo('#conteudo_panel').hide()
});
jQuery(document).ajaxStart(function(){ 
    jQuery('#loading').show(); 
}).ajaxStop(function(){ 
  jQuery('#loading').hide();
});
