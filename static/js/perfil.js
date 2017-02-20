var pagina_archivo = 1;
var image_icono_upload = $('.subir_archivo').attr('src');
var input = document.createElement('input');
input.type = "file";
input.name = "archivo";

var form = document.createElement("form");
form.setAttribute('method', 'post');
form.setAttribute('enctype','multipart/form-data');


var etiqueta = 'image';

$(function(){
    $('#experiencia, #audio,#video, #image').click(function(){
        etiqueta = $(this).attr('id');
        $('.link_galeria').removeClass('activo');
        $(this).addClass('activo');
        $('.galerias').fadeOut();
        $('#gallery-'+etiqueta).fadeIn();
        x = etiqueta
        if(x == 'image'){
            x = 'imagen';
        }

        $('#titulo_modal_subir_archivo').text(x);
    });
    paginacion_archivo(pagina_archivo, false, 'image');
    paginacion_archivo(pagina_archivo, false, 'audio');
    $('.subir_archivo').click(function(){

        $(input).click();
    });
    $(input).change(function(e){
        NProgress.start();
        $('.ivo-mensaje-contenedorAudio-contenido2').text(0+" %");

        if(etiqueta == 'fotos'){
            handleFileSelect(e);
        }else {
            subirArchivoAudioVideo(e);
        }

    });
});

function handleFileSelect(evt) {
    var files = evt.target.files[0]; // FileList object

    if (files.type == 'image/jpg' || files.type == 'image/jpeg' || files.type == 'image/png' || files.type == 'image/gif') {
        var reader = new FileReader();

        reader.onload = (function (theFile) {
            return function (e) {
                var image = new Image();
                image.src = e.target.result;

                image.onload = function () {
                    if (image.width < 400) {
                        alert("Por favor ingrese una imagen mas grande, la medida minima son de 400 x 300");
                        return false;
                    } else if (image.height < 300) {
                        alert("Por favor ingrese una imagen mas grande, la medida minima son de 400 x 300");
                        return false;
                    }
                    //console.log(image.width);
                    var canvas = document.createElement('canvas');
                    var ctx = canvas.getContext("2d");
                    ctx.drawImage(image, 0, 0);
                    var MAX_WIDTH = 350;
                    var MAX_HEIGHT = 200;
                    var width = image.width;
                    var height = image.height;
                    if (width > height) {
                        if (width > MAX_WIDTH) {
                            height *= MAX_WIDTH / width;
                            width = MAX_WIDTH;
                        }
                    } else {
                        if (height > MAX_HEIGHT) {
                            width *= MAX_HEIGHT / height;
                            height = MAX_HEIGHT;
                        }
                    }
                    canvas.width = width;
                    canvas.height = height;
                    var ctx = canvas.getContext("2d");
                    ctx.drawImage(this, 0, 0, width, height);                    
                    var dataurl = canvas.toDataURL("image/jpg");
                    $('.subir_archivo').attr('src',dataurl);

                    subirArchivo('imagen');
                };
            };
        })(files);

        reader.readAsDataURL(files);

    }else{
        alert("Archivo no soportado");
    }

}
function subirArchivoAudioVideo(evt) {
    var files = evt.target.files[0];
    if(etiqueta == 'audio'){
        console.log(files);
        if (files.type != 'audio/mp3' && files.type != 'audio/mp4' && files.type != 'audio/WebM' &&
            files.type != 'audio/ogg' && files.type != 'audio/mpeg' ) {
            NProgress.done();
            alert('Formato de archivo no soportado');
            return;
        }
    }else if(etiqueta == 'video'){
        if (files.type != 'video/webm' && files.type != 'video/ogg' && files.type != 'video/mp4') {
            NProgress.done();
            alert('Formato de archivo no soportado');
            return;
        }
    }
    subirArchivo(etiqueta)

}
function subirArchivo(tipo_archivo){
    $(form).append($(input));
    $(form).append($('#csrf'));
    var formData = new FormData($(form)[0]);
    var ruta = '/perfil/subir_archivo/'+tipo_archivo+'/';
    $.ajax({
        url: ruta,
        type: "POST",
        dataType: "json",
        data: formData,
        cache: false,
        contentType: false,
        processData: false,

        xhr: function() {
            var myXhr = $.ajaxSettings.xhr();
            if (myXhr.upload) {
                myXhr.upload.addEventListener('progress',function(ev) {
                    if (ev.lengthComputable) {
                        var percentUploaded = Math.floor(ev.loaded * 100 / ev.total);
                        $('.ivo-mensaje-contenedorAudio-carga').css({'width' : percentUploaded+"%"});
                        $('.ivo-mensaje-contenedorAudio-contenido2').text(percentUploaded+" %");
                        // update UI to reflect percentUploaded
                    }
                }, false);
            }
            return myXhr;
        },
        success: function(datos){
            $('#progreso_subida').css({'width' : "0%"});
            $('#porcentaje_subida').text("0 %");
            NProgress.done();

            $('#SubirFoto').modal('hide');
            paginacion_archivo(pagina_archivo,true, tipo_archivo);
        },
        error: function (err) {
            NProgress.done();
        }

    })
}

function paginacion_archivo(nro_pagina, mover_scroll, tipo_archivo){
    console
    pagina_archivo = nro_pagina;
    NProgress.start();
    $.ajax({
        url: '/perfil/buscar-multimedia/'+tipo_archivo+'/',
        type: 'get',
        dataType: 'json',
        async: true,
        data: {page:nro_pagina},
        success: function (data){
            if (mover_scroll ==true){
                $("html, body").animate({ scrollTop: '700px'}, 1000);     
            }
            NProgress.done();
            if(data.mensaje == ''){
                if(tipo_archivo == 'imagen' || tipo_archivo == 'image'){
                    $('#gallery-image').html(data.archivos);
                }else if(tipo_archivo == 'audio'){
                    $('#gallery-audio').html(data.archivos);
                }else if(tipo_archivo == 'audio'){
                    $('#gallery-audio').video(data.archivos);
                }

                $('#item_paginas').html(data.item_paginas)
            }
        }
    });
}

/**********  reproductor de audio **********/
var audio = new Audio();
var barraProgreso;
var suena_audio = false;
var audio_current = '';
var audio_duracion
$(function(){
    audio.addEventListener('timeupdate', function() {
        duracion = parseInt(audio.currentTime);
        segundos_d =  duracion%60;
        minutos_d  = parseInt(duracion/60);

        if(segundos_d <10) segundos_d = '0' +  duracion%60;
        if(minutos_d <10) minutos_d = '0' +  parseInt(duracion/60);
        audio_duracion.text(minutos_d + ":" + segundos_d);


        avance = (audio.currentTime * 100 ) / audio.duration;
		barraProgreso.css({'width' : avance+"%"});

        if(audio.currentTime == audio.duration){
            $('.tiempo').text("00:00");
            $('.ivo-mensaje-contenedorAudio-carga').css({'width' : '0%'});
            $('.ivo-mensaje-contenedorAudio-contenido > div >span').addClass('arrow_triangle-right_alt');
            $('.ivo-mensaje-contenedorAudio-contenido > div >span').removeClass('icon_pause_alt2');
        }

    }, true);
    audio.addEventListener("load", function() {
       audio.play();
    }, true);
    $(document).on("click",".play_audio", function(){

        indx = $(this).attr('id');
        barraProgreso = $('#progreso_audio-'+indx);
        audio.src = $(this).attr('audio');
        audio_duracion = $('#tiempo_audio-'+indx);

        if(audio_current == ''){
            suena_audio = true;
            audio_current = $(this).attr('audio');
            audio.play();
            $(this).removeClass('arrow_triangle-right_alt');
            $(this).addClass('icon_pause_alt2');

            return;
        }
        if(suena_audio && audio_current == $(this).attr('audio')){
            $(this).addClass('arrow_triangle-right_alt');
            $(this).removeClass('icon_pause_alt2');
            suena_audio = false;
            audio.pause();
        }else if(audio_current == $(this).attr('audio')){
            suena_audio = true;
            audio.play();
        }else{
            suena_audio = true;
            audio_current = $(this).attr('audio');

            $('.tiempo').text("00:00");
            $('.ivo-mensaje-contenedorAudio-carga').css({'width' : '0%'});
            $('.ivo-mensaje-contenedorAudio-contenido > div >span').addClass('arrow_triangle-right_alt');
            $('.ivo-mensaje-contenedorAudio-contenido > div >span').removeClass('icon_pause_alt2');

            $(this).removeClass('arrow_triangle-right_alt');
            $(this).addClass('icon_pause_alt2');

            audio.play();
        }
    });


})