<template>
    <body >
    <div class="page-wrapper">
        <div class="container">
          <div class="login-wrap">
            <div class="login-content" style="margin-top: 150px">
              <div class="login-logo">
                <a href="#">
                  <img src="../assets/images/icon/logo.png" alt="CoolAdmin">
                </a>
              </div>
              <div class="login-form">
                <form @submit.prevent="login">
                  <div class="form-group">
                    <label>Username</label>
                    <input class="au-input au-input--full" type="text" v-model="username" id="username" required placeholder="Username">
                  </div>
                  <div class="form-group">
                    <label>Password</label>
                    <input class="au-input au-input--full" type="password" v-model="password" id="password" required placeholder="Password">
                  </div>
                  <p v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</p>
                  <button class="au-btn au-btn--block au-btn--green m-b-20" type="submit">Connexion</button>
                </form>

              </div>
            </div>
          </div>
        </div>
      </div>



    </body>

</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/api/user/login', {
          username: this.username,
          password: this.password,
        });

        const token = response.data.access_token;
        localStorage.setItem('token', token);  // Sauvegarde le token pour l'utiliser dans d'autres requêtes
        this.$router.push('/Dashboard');  // Redirige vers une autre page après le login
      } catch (error) {
        this.errorMessage = 'Identifiants Incorrects';
      }
    },
  },
};
</script>
