<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <q-page>
        <div class="wrapper">
          <q-card class="card q-pa-xl">
            <q-form @submit="loginSubmit" class="q-gutter-md">
              <q-input v-model="user.username" label="Username" :rules="[val => !!val || 'Field is required']"></q-input>
              <q-input v-model="user.password" type="password" label="Password" :rules="[val => !!val || 'Field is required']"></q-input>
              <q-btn type="submit">Sign Up</q-btn>
            </q-form>
          </q-card>
        </div>

      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import {IUserLogin} from "stores/authStoreTypes";
import {reactive} from "vue";
import {useAuthStore} from "stores/authStore";

const authStore = useAuthStore()

const user: IUserLogin = reactive({
  username: '',
  password: ''
})
const loginSubmit = async () =>{
  await authStore.login(user.username,user.password)
}
</script>

<style scoped lang="scss">
.card {
  width: 400px;
  max-width: 400px;
}
.wrapper {
  width: 100vw;
  height: 100vh;

  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
