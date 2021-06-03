
function onLoadHide() {
    document.getElementById("perkm1").style.display = "block";
    document.getElementById("perkm2").style.display = "block";
    document.getElementById("perkm3").style.display = "block";
    document.getElementById("ifCadence1").style.display = "block";
    document.getElementById("ifCadence2").style.display = "block";
    document.getElementById("ifCadence3").style.display = "block";
    document.getElementById("ifDSteps1").style.display = "none";
    document.getElementById("ifDSteps2").style.display = "none";
    document.getElementById("ifDSteps3").style.display = "none";
    document.getElementById("ifDistance1").style.display = "none";
    document.getElementById("ifDistance2").style.display = "none";
    document.getElementById("ifDistance3").style.display = "none";
    document.getElementById("progressBar").style.display = "none";
    document.getElementById("cadencecalc").style.display = "none";
    document.getElementById("librarybrowse").style.display = "none";
    document.getElementById("topbrowse").style.display = "none";
    document.getElementById("recentbrowse").style.display = "none";
    document.getElementById("playlistcreate").style.display = "none";
    document.getElementById("playlistadd").style.display = "none";
}


function yesnoCheck(that) {
   
    if (that.value == "DistanceAndSteps") {

        document.getElementById("ifDistance1").style.display = "block";
        document.getElementById("ifDistance2").style.display = "block";
        document.getElementById("ifDistance3").style.display = "block";
        document.getElementById("ifDSteps1").style.display = "block";
        document.getElementById("ifDSteps2").style.display = "block";
        document.getElementById("ifDSteps3").style.display = "block";
        document.getElementById("perkm1").style.display = "none";
        document.getElementById("perkm2").style.display = "none";
        document.getElementById("perkm3").style.display = "none";
        document.getElementById("ifCadence1").style.display = "none";
        document.getElementById("ifCadence2").style.display = "none";
        document.getElementById("ifCadence3").style.display = "none";

    } else {
    
        document.getElementById("perkm1").style.display = "block";
        document.getElementById("perkm2").style.display = "block";
        document.getElementById("perkm3").style.display = "block";
        document.getElementById("ifCadence1").style.display = "block";
        document.getElementById("ifCadence2").style.display = "block";
        document.getElementById("ifCadence3").style.display = "block";
        document.getElementById("ifDSteps1").style.display = "none";
        document.getElementById("ifDSteps2").style.display = "none";
        document.getElementById("ifDSteps3").style.display = "none";
        document.getElementById("ifDistance1").style.display = "none";
        document.getElementById("ifDistance2").style.display = "none";
        document.getElementById("ifDistance3").style.display = "none";

}

}
var i = 0;
function loading() {
    document.getElementById("progressBar").style.display = "block";
    document.getElementById("user_input_form").style.display = "none";
    document.getElementById("intro").style.display = "none";
    document.getElementById("CadenceorNot").style.display = "none";
    if (i == 0) {
        
        i = 1;
        var elem = document.getElementById("myBar");
        var width = 1;
        var id = setInterval(frame, 20000);
        function frame() {
            if (width >= 100) {
            clearInterval(id);
            i = 0;
            if (elem.style.width < 10) {
                document.getElementById("cadencecalc").style.display = "block";
                document.getElementById("librarybrowse").style.display = "none";
                document.getElementById("topbrowse").style.display = "none";
                document.getElementById("recentbrowse").style.display = "none";
                document.getElementById("playlistcreate").style.display = "none";
                document.getElementById("playlistadd").style.display = "none";
            }
            if (elem.style.width < 30) {
                document.getElementById("cadencecalc").style.display = "none";
                document.getElementById("librarybrowse").style.display = "block";
                document.getElementById("topbrowse").style.display = "none";
                document.getElementById("recentbrowse").style.display = "none";
                document.getElementById("playlistcreate").style.display = "none";
                document.getElementById("playlistadd").style.display = "none";
            }
            if (elem.style.width < 50) {
                document.getElementById("cadencecalc").style.display = "none";
                document.getElementById("librarybrowse").style.display = "none";
                document.getElementById("topbrowse").style.display = "block";
                document.getElementById("recentbrowse").style.display = "none";
                document.getElementById("playlistcreate").style.display = "none";
                document.getElementById("playlistadd").style.display = "none";
            }
            if (elem.style.width < 70) {
                document.getElementById("cadencecalc").style.display = "none";
                document.getElementById("librarybrowse").style.display = "none";
                document.getElementById("topbrowse").style.display = "none";
                document.getElementById("recentbrowse").style.display = "block";
                document.getElementById("playlistcreate").style.display = "none";
                document.getElementById("playlistadd").style.display = "none";
            }
            if (elem.style.width < 90) {
                document.getElementById("cadencecalc").style.display = "none";
                document.getElementById("librarybrowse").style.display = "none";
                document.getElementById("topbrowse").style.display = "none";
                document.getElementById("recentbrowse").style.display = "none";
                document.getElementById("playlistcreate").style.display = "block";
                document.getElementById("playlistadd").style.display = "none";
            }
            if (elem.style.width <= 100) {
                document.getElementById("cadencecalc").style.display = "none";
                document.getElementById("librarybrowse").style.display = "none";
                document.getElementById("topbrowse").style.display = "none";
                document.getElementById("recentbrowse").style.display = "none";
                document.getElementById("playlistcreate").style.display = "none";
                document.getElementById("playlistadd").style.display = "block";
            }
        } else {
            width++;
            elem.style.width = width + "%";
            
        }
        }
        
    }
    
}