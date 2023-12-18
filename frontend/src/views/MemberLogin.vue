<template>
    <div class="div">
      <div class="div-2">
        <div class="div-3">Qrade</div>
        <img
          loading="lazy"
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/fe0b6d2c0026ce9c5faa311c85954a4b7b268fd085ae93a9c8d654e509345a4a?"
          class="img"
        />
        <div class="div-4"  @submit.prevent="handleLogin">Log in</div>
        <form id="loginForm" act>
          <input type="text" v-model="user_id" name="user_id" class="div-5" placeholder="id">
          <br><br>
          <input type="password" v-model="password" name="password" class="div-6" placeholder="password ">
          <br><br>
          <button type="submit" class="div-10">Log in</button>
      </form>
      <label >
        <br>
        <input type="checkbox" name="remember_me">
        Remember me
        <br>
      </label>
      
        
        <button type="button" id='kakaoLogin' class = "div-11" @click="kakaoLogin()">
          <img src="../../src\assets\kakao_login_medium_wide.png" alt="Button Image" />
          </button>
          <div>
            <button type="button" id='kakaoLogout' class = "div-11" @click="kakaoLogout()">
          로그아웃
          </button>
  </div>
      </div>
    </div>
  </template>

<script>
  
  export default {

    data() {
    return {
      loginData: {
        username: '',
        password: ''
      }
    };
  },
    methods: {
    kakaoLogin() {
      window.Kakao.Auth.login({
        scope: "profile_image",
        success: this.getKakaoAccount,
        redirectUri:"http://localhost:8080/auth/callback"
      });
    },
    getKakaoAccount() {
      window.Kakao.API.request({
        url: "/v2/user/me",
        success: (res) => {
          const kakao_account = res.kakao_account;
          const ninkname = kakao_account.profile.ninkname;
          
          console.log("ninkname", ninkname);
          

          //로그인처리구현

          alert("로그인 성공!  "+ninkname);
        },
        fail: (error) => {
          console.log(error);
        },
      });
    },
    kakaoLogout() {
      window.Kakao.Auth.logout((res) => {
        console.log(res);
      });
    },
  },
};
</script>

  
  
  <style scoped>
  .div {
    background-color: #fff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 50px 60px;
  }
  @media (max-width: 991px) {
    .div {
      padding: 0 20px;
    }
  }
  .div-2 {
    display: flex;
    width: 400px;
    max-width: 100%;
    flex-direction: column;
    margin: 176px 0 452px;
  }
  @media (max-width: 991px) {
    .div-2 {
      margin: 40px 0;
    }
  }
  .div-3 {
    color: var(--Colour-Logo-Primary, #2245e3);
    font-feature-settings: "clig" off, "liga" off;
    align-self: center;
    white-space: nowrap;
    font: 900 40px/95% Roboto, sans-serif;
  }
  @media (max-width: 991px) {
    .div-3 {
      white-space: initial;
    }
  }
  .img {
    aspect-ratio: 400;
    object-fit: contain;
    object-position: center;
    width: 100%;
    stroke-width: 1px;
    stroke: #a3a3a3;
    overflow: hidden;
    align-self: stretch;
    margin-top: 19px;
  }
  .div-4 {
    color: #000;
    align-self: center;
    margin-top: 46px;
    white-space: nowrap;
    font: 400 30px/150% Inter, sans-serif;
  }
  @media (max-width: 991px) {
    .div-4 {
      margin-top: 40px;
      white-space: initial;
    }
  }
  .div-5 {
    color: #858585;
    white-space: nowrap;
    border-radius: 8px;
    border: 1px solid #a3a3a3;
    align-self: stretch;
    margin-top: 16px;
    width: 100%;
    justify-content: center;
    align-items: start;
    padding: 16px 60px 16px 14px;
    font: 400 18px/150% Inter, sans-serif;
  }
  @media (max-width: 991px) {
    .div-5 {
      white-space: initial;
      padding-right: 20px;
      margin: 0 7px;
    }
  }
  .div-6 {
    color: #858585;
    white-space: nowrap;
    border-radius: 8px;
    border: 1px solid #a3a3a3;
    align-self: stretch;
    margin-top: 12px;
    width: 100%;
    justify-content: center;
    align-items: center;
    padding: 16px 60px 16px 14px;
    font: 400 18px/150% Inter, sans-serif;
  }
  @media (max-width: 991px) {
    .div-6 {
      white-space: initial;
      padding-right: 20px;
      margin: 0 7px;
    }
  }
  .div-7 {
    align-self: start;
    display: flex;
    margin-top: 29px;
    gap: 5px;
  }
  .div-8 {
    border-radius: 4px;
    border: 1px solid #a3a3a3;
    background-color: #fff;
    display: flex;
    width: 16px;
    height: 16px;
    flex-direction: column;
  }
  .div-9 {
    color: #5e5e5e;
    align-self: center;
    flex-grow: 1;
    white-space: nowrap;
    margin: auto 0;
    font: 400 10px/150% Inter, sans-serif;
  }
  @media (max-width: 991px) {
    .div-9 {
      white-space: initial;
    }
  }
  .div-10 {
    color: #fff;
    white-space: nowrap;
    border-radius: 8px;
    border: 1px solid #a3a3a3;
    background-color: #2245e3;
    align-self: center;
    margin-top: 5px;
    width: 100%;
    max-width: 100%;
    justify-content: center;
    align-items: center;
    padding: 14px 60px;
    font: 400 18px/150% Inter, sans-serif;
  }
  @media (max-width: 991px) {
    .div-10 {
      white-space: initial;
      padding: 0 20px;
    }
  }
  .div-11 {
    background-color: #FEE602;
    display: flex;
    width: 100%;
    max-width: 100%;
    justify-content: center;
    align-items: center;
    border: none;
  }
  @media (max-width: 991px) {
    .div-11 {
      justify-content: center;
      align-items: center;
    }
  }
  .img-2 {
    aspect-ratio: 170;
    object-fit: contain;
    object-position: center;
    width: 170px;
    stroke-width: 1px;
    stroke: #a3a3a3;
    overflow: hidden;
    align-self: center;
    max-width: 100%;
    margin: auto 0;
  }
  .div-12 {
    color: #a3a3a3;
    font-feature-settings: "clig" off, "liga" off;
    font: 400 15px/253% Roboto, sans-serif;
  }
  .img-3 {
    aspect-ratio: 170;
    object-fit: contain;
    object-position: center;
    width: 170px;
    stroke-width: 1px;
    stroke: #a3a3a3;
    overflow: hidden;
    align-self: center;
    max-width: 100%;
    margin: auto 0;
  }
  .img-4 {
    aspect-ratio: 7.76;
    object-fit: contain;
    object-position: center;
    width: 295px;
    overflow: hidden;
    align-self: center;
    margin-top: 29px;
    max-width: 100%;
  }
  </style>