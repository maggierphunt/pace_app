
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
        var id = setInterval(frame, 5000);
        function frame() {
        if (width >= 100) {
            clearInterval(id);
            i = 0;
        } else {
            width++;
            elem.style.width = width + "%";
        }
        }
    }
    
}