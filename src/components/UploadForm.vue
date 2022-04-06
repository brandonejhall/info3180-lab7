<template >
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
            csrf_token: '',
            success: '',
            error = []          
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
            self.success = data.message
            
            })
            .catch(function (error) {
            console.log(error);
            self.error = error.message
            
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
