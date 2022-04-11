function ready ()
{
    var inputFile = document.querySelectorAll(".inputfile");
    Array.prototype.forEach.call(inputFile, function( input )
    {
        var label = input.nextElementSibling,
        labelVal = label.innerHTML;

        input.addEventListener('change', function ( e )
        {
            console.log(this.files);
            var fileName = '';
            if( this.files && this.files.length > 1 )
                fileName = ( this.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', this.files.length );
            else
                fileName = this.files[0].name;
            
            if( fileName )
                label.querySelector( 'span' ).innerHTML = fileName;
            else
                label.innerHTML = labelVal;
        });
    });
};

document.addEventListener("DOMContentLoaded", ready);