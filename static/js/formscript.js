
function yesnoCheck(that) {
    if (that.value == "DistanceAndSteps") {

        document.getElementById("ifDistance1").style.display = "block";
        document.getElementById("ifDistance2").style.display = "block";
        document.getElementById("ifDistance3").style.display = "block";
        document.getElementById("running1").style.display = "block";
        document.getElementById("running2").style.display = "block";
        document.getElementById("running3").style.display = "block";
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
        document.getElementById("running1").style.display = "none";
        document.getElementById("running2").style.display = "none";
        document.getElementById("running3").style.display = "none";

}

}