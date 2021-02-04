<?php
date_default_timezone_set("Europe/Istanbul");
echo "Time is : " , (date("H:i:s")) , "<br>";
$forMessage = date("H");

switch ($forMessage){
    case (06<=$forMessage && $forMessage<10):
        echo "Günaydın";
    break;
    case (10<=$forMessage && $forMessage<17):
        echo "İyi günler";
    break;
    case (17<=$forMessage && $forMessage<20):
        echo "İyi akşamlar";
    break;
    case (20<=$forMessage && $forMessage<24):
        echo "İyi geceler";
    break;
    case (00<=$forMessage && $forMessage<06):
        echo "Esenlikler dilerim";
    break;
}
?>