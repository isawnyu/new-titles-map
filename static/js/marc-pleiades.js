// See post: http://asmaloney.com/2015/06/code/clustering-markers-on-leaflet-maps

// Sets up map to include widest stretch between Atlantic and Pacific Oceans
var map = L.map( 'map', {
		center: [40, 53],
		zoom: 3,
		minZoom: 3,
		maxZoom: 8,
		zoomControl: false
});

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiaXNhd255dSIsImEiOiJBWEh1dUZZIn0.SiiexWxHHESIegSmW8wedQ', {
 attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
 maxZoom: 10,
 id: 'isawnyu.map-knmctlkh',
 accessToken: 'pk.eyJ1IjoiaXNhd255dSIsImEiOiJja2FoNWxhbGMwZ2EzMnhxaDNweWhuaXFkIn0.CVcdizYVocm7c0PY1OOn1Q'
 
 }).addTo(map);

var newControl = new L.Control.ZoomMin()
map.addControl(newControl)

var myURL = jQuery( 'script[src$="marc-pleiades.js"]' ).attr( 'src' ).replace( 'marc-pleiades.js', '' );

var myIcon = L.icon({
	iconUrl: myURL + '../img/pin24.png',
	iconRetinaUrl: myURL + '../img/pin48.png',
	iconSize: [29, 24],
	iconAnchor: [9, 21],
	popupAnchor: [0, -14]
});

var markerClusters = L.markerClusterGroup();

for ( var i = 0; i < books.length; ++i )
{
		
		if (books[i].pleiades_id != "") {
				var pleiadesLink = '<br/><b>Pleiades link:</b> <a href="https://pleiades.stoa.org/places/' + books[i].pleiades_id + '" target="_blank">' + books[i].pleiades_name + ' ' + books[i].pleiades_id + '</a>';
				
		} else {
				pleiadesLink = "";
		}
		
		if (books[i].series != "") {
				var seriesContent = '<b>Series:</b> ' + books[i].series + '<br/>';
		} else {
				seriesContent = "";
		}
		
		
		bsn = books[i].bsn
		pad = '000000000'
		bsn = (pad+bsn).slice(-pad.length);   // Pads the string with leading zeros to make its length = 9
		bobcatLink = 'https://library.nyu.edu/persistent/lcn/nyu_aleph' + bsn + '?institution=NYU&persistent';
		
	var popup = L.popup()
				.setContent(
						'<b>Title and author:</b> ' + books[i].title + '<br/>' +
						'<b>Imprint:</b> ' + books[i].imprint + '<br/>' +
						seriesContent +
						'<b>ISAW Shelving Location:</b> ' + books[i].shelf_location + '<br/>' +
						'<a href="' + bobcatLink + '" target="_blank">View in NYU catalog</a>' + '<br/>' +
						pleiadesLink + '<br/>' +
						'<b>Region:</b> ' + books[i].region + ' <b>Location:</b> ' + books[i].location + '<br/>' +
						'<b>Representative coordinates:</b> ' + books[i].latitude + ',' + books[i].longitude + '</br>')
		
		if (books[i].latitude != "" || books[i].longitude != "" ) {
				var m = L.marker( [books[i].latitude, books[i].longitude], {icon: myIcon} )
									.bindPopup( popup, {minWidth: 400} );
		} else {
				console.log(books[i].book + ' does not have correct.latitude-long information.')
		}

	markerClusters.addLayer( m );
}

map.addLayer( markerClusters );
