/**
*
*  Add picasa gallery to your blog or website
*  http://www.webtoolkit.info/
*
**/
var picasa = { 
    galleries: 0, 
    gallery: function (galleryObjectId, galleryObjectName, settings) {
        this.galleryObjectId = galleryObjectId;
        this.galleryObjectName = galleryObjectName;
        this.containerId = settings.containerId;
        this.userName = settings.userName;
        this.albumName = settings.albumName;
        this.imageSize = settings.imageSize;
        this.itemsArray = [];
        this.setup = function (data) {
            this.itemsArray = data.feed.entry;
            this.totalItems = this.itemsArray.length;
            // Initial values setup.
            jQuery('#photo_img').attr('src', this.itemsArray[0].media$group.media$content[0].url);
            jQuery('#photo_descr').text(this.itemsArray[0].media$group.media$description.$t);
            
            for (var x = 0; x < this.totalItems; x++) {
                jQuery('#' + this.containerId).append('<li><a href="#photo" onclick="set_picture(\'' + this.itemsArray[x].media$group.media$content[0].url+'\', \'' + this.itemsArray[x].media$group.media$description.$t + '\');"><img src=\'' + this.itemsArray[x].media$group.media$thumbnail[0].url+ '\'" class="photo_icon" "/></a></li>');
            }
        };
    },
    load: function (settings) {
        var galleryObjectId = picasa.galleries++;
        var galleryObjectName = 'picasa.gallery' + galleryObjectId;
        var galleryObject = eval(galleryObjectName + ' = new picasa.gallery(galleryObjectId, galleryObjectName, settings)');
        scriptLoader.load([
            'http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js',
            'http://picasaweb.google.com/data/feed/api/user/' + galleryObject.userName + '/album/' + galleryObject.albumName + '?alt=json-in-script&callback=' + galleryObjectName + '.setup&kind=photo&thumbsize=' + galleryObject.imageSize
        ]);
    }
}
function set_picture(obj_url, obj_caption){
    jQuery('#photo_img').attr('src', obj_url);
    jQuery('#photo_descr').text(obj_caption);
}
