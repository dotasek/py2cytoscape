if (window['cytoscape'] === undefined) {
    var paths = {
        cytoscape: 'https://rawgit.com/cytoscape/cytoscape.js/master/dist/cytoscape'
    };

    require.config({
        paths: paths
    });

    require(['cytoscape'], function (cytoscape) {
        console.log('Loading Cytoscape.js Module...');
        window['cytoscape'] = cytoscape;

        var event = document.createEvent("HTMLEvents");
        event.initEvent("load_cytoscape", true, false);
        window.dispatchEvent(event);
    });

}
