"use-strict";

var audio1 = new Audio();
audio1.src="./tom-1.mp3";
const btnd = document.querySelector(".d");
btnd.addEventListener("click", 
function(e){
    e.preventDefault();
    audio1.play();
})

var audio2 = new Audio();
audio2.src="./crash.mp3";
const btnr = document.querySelector(".r");
btnr.addEventListener("click", 
function(e){
    e.preventDefault();
    audio2.play();
})

var audio3 = new Audio();
audio3.src="./snare.mp3";
const btnu = document.querySelector(".u");
btnu.addEventListener("click", 
function(e){
    e.preventDefault();
    audio3.play();
})

var audio4 = new Audio();
audio4.src="./kick-bass.mp3";
const btnm = document.querySelector(".m");
btnm.addEventListener("click", 
function(e){
    e.preventDefault();
    audio4.play();
})

var audio5 = new Audio();
audio5.src="./tom-2.mp3";
const btnk= document.querySelector(".k");
btnk.addEventListener("click", 
function(e){
    e.preventDefault();
    audio5.play();
})

var audio6 = new Audio();
audio6.src="./tom-3.mp3";
const btni = document.querySelector(".i");
btni.addEventListener("click", 
function(e){
    e.preventDefault();
    audio6.play();
})

var audio7 = new Audio();
audio7.src="./tom-4.mp3";
const btnt = document.querySelector(".t");
btnt.addEventListener("click", 
function(e){
    e.preventDefault();
    audio7.play();
});





