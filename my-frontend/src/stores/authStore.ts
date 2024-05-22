import {defineStore} from "pinia";
import {IAuthStore, IUserLogin} from "stores/authStoreTypes";
import {api} from "boot/axios";
import {loginEndpoint} from "src/api";
import {Notify} from "quasar";

export const useAuthStore = defineStore('auth', {
  state: (): IAuthStore => ({
    token: '',
    isAuthenticated: false,
  }),
  actions: {
    async login(username: string, password: string) {
      const loginData: IUserLogin = {username: username, password: password}
      try {
        const response = await api.post(loginEndpoint, loginData)
        this.token = response.data.authorization
        this.isAuthenticated = true
        api.defaults.headers['Authorization'] = this.token
        this.router.push({name:'article-list'})
      } catch (error: unknown) {
        Notify.create({
          color: 'negative',
          message: 'Something went wrong. Maybe your credentials are incorrected',
        })
      }
    }

  }
})
