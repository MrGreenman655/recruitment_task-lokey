export interface IAuthStore {
  token: string,
  isAuthenticated: boolean,
}

export interface IUserLogin {
  username: string,
  password: string,
}
