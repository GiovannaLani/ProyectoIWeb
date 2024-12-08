var app = new Vue({
    el:'#contacto',
    data:{
            newNombre:'',
            newEmail:'',
            newTelefono:'',
            contactos: [{
                nombre:'John Doe',
                email:'john.doe@deusto.es',
                telefono:555555555
            }]
        },
    methods:{
        saveContactos: function(event){

            if (this.newNombre.trim() === '' || this.newEmail.trim() === '' || this.newTelefono.trim() === '') {
                alert('Todos los campos son obligatorios');
                return;
            }
            this.contactos.push( { nombre: this.newNombre, email: this.newEmail, telefono: this.newTelefono} );
            this.newNombre = "";
            this.newEmail = "";
            this.newTelefono = "";
            },
        removeContactos: function(index){
            this.contactos.splice(index, 1);
            }
        }
    })