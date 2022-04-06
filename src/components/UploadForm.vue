<template >
    <div class = 'alert enotifs' v-if="errors.length">
        <ul>
            <li v-for="error in errors" :key = 'error'>{{ error }}</li>
        </ul>
    </div>
    <div class = 'alert snotifs' v-else-if = "message.length">
        <p id  = "success" >{{message}}</p>
    </div>
    
    <form id = "uploadForm" action = '' method = 'POST' @submit.prevent="uploadPhoto" enctype="multipart/form-data">

    <div class = "data">
        <label for="description">Description: </label>
        <input type="text" id="description" name="description"><br><br>
    </div>
    <div class = "data">
        <label for="image">Image: </label>
        <input type="file" id="image" name="image"><br><br>
    </div>
    <div class = "data">
        <input type="submit" value="Submit">
    </div>
    </form>
</template>

<script>
export default {
    data() {
        return {
            message: '',
            errors: [],
            csrf_token: ''
        }
    },
    methods: {
        uploadPhoto(){
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);
            let self = this;
            fetch("/api/upload", {
            method: 'POST',
            body:form_data,
            headers: {'X-CSRFToken': this.csrf_token}
            })
            .then(function (response) {
            return response.json();
            })
            .then(function (data) {
            // display a success message
            console.log(data);
            self.message = data.message
            
            })
            .catch(function (error) {
            console.log(error);
            self.errors = error
            
        });
        },

        getCsrfToken(){
            let self = this;
            fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
            console.log(data);
            self.csrf_token = data.csrf_token;
            });
        }
    },
    created() {
        this.getCsrfToken();
    }
}
</script>

<style>
.alert{
    position: relative;
    padding: 0.75rem 1.25rem;
    margin-bottom: 1rem;
    border: 1px solid transparent;
    border-radius: 0.25rem;
}
.snotifs{
    color: #155724;
    background-color: #d4edda;
    border-color: #c3e6cb;
}
.enotifs{
    color: #721c24;
    background-color: #f8d7da;
    border-color: #f5c6cb;
}
</style>