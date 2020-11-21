<template>
  <div id="login">
    <v-app id="sublogin">

      <h2>Вход в личный кабинет</h2>
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
    
        <v-text-field
          v-model="email"
          :rules="emailRules"
          label="E-mail"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          :rules="passwordRules"
          label="Password"
          type="password"
          required
        ></v-text-field>

        <v-btn
          :disabled="!valid"
          color="primary"
          class="mr-4"
          @click="validate"
        >
          Войти
        </v-btn>
    
        <v-btn
          color="error"
          class="mr-4"
          @click="reset"
        >
          Очистить
        </v-btn>
      </v-form>
  </v-app>
  </div>
</template>

<script>

  export default {
    data: () => ({
      valid: true,
      password: '',
      passwordRules: [
        v => !!v || 'Пароль не может быть пустым',
        v => (v && v.length > 10) || `Пароль должен быть длиннее 10 символов, а сейчас ${v.length}`,
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail не может быть пустым',
        v => /.+@.+\..+/.test(v) || 'Введите корректный e-mail',
      ]
    }),

    methods: {
      validate () {
        if (this.$refs.form.validate()){
          this.$router.push('/')
        }
      },
      reset () {
        this.$refs.form.reset()
      }
    }
  }
</script>

<style scoped>
  #login{
    display: flex;
    min-width: 1500px;
    height: 725px;
    margin: auto auto;
    overflow-y: hidden;
  }
  #sublogin{
      margin: auto auto;
      min-width: 700px;
      height: 250px;
      padding: 15px 15px;
      border: 1px;
      border-radius: 10px;
  }
</style>