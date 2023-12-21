<template>
    <div class="div">
      <div class="div-2">
        <div class="div-3">회원 가입</div>
        <form id="loginForm" @submit.prevent="memberJoin()">
          <br>
          <label for="name">이름</label>
          <input type="text" v-model="name" name="name" class="div-5" placeholder="user_name" required>
          <br><br>
          <label for="id">아이디</label>
          <input type="text" v-model="id" name="id" class="div-5" placeholder="id" required>
          <br><br>
          <label for="password">비밀번호</label>
          <input type="password" v-model="password" name="password" class="div-5" placeholder="password " required>
          <br><br>
          <label for="kakao_nick_name">카카오톡 닉네임</label>
          <input type="text" v-model="kakao_nick_name"  name="kakao_nick_name" value="none"  class="div-6"  >
          <br><br>
          <button type="submit" class="div-10">memberJoin</button>
      </form>

      </div>
    </div>
  </template>
  
  <script>
    import fastapi from "../lib/api"

  export default {
    

    data() {
    return {
      loginData: {
        id:'',
        username: '',
        password: '',
        kakao_nick_name: ''
      }
    };
  },
    methods: {
        memberJoin(){
          let url ="/memberJoin"
          let params={
            _id:this.id,
            password:this.password,
            name:this.name,
            kakao_nick_name:this.kakao_nick_name
          }
          
          fastapi('post', url, params,
            () => {
              this.$router.push("/")
            },
            (json_error) => {
              this.error = json_error
            })
            
        }
    
    }
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
    width: 386px;
    max-width: 100%;
    flex-direction: column;
    margin: 160px 0 462px;
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
    margin-top: 16px;
    width: 100%;
    justify-content: center;
    align-items: start;
    padding: 16px 60px 16px 14px;
    font: 400 18px/150% Inter, sans-serif;
    opacity: 0.4;
  }
  @media (max-width: 991px) {
    .div-5 {
      white-space: initial;
      padding-right: 20px;
      margin: 0 7px;
    }
  }
  
  .div-7 {
    color: #fff;
    white-space: nowrap;
    border-radius: 8px;
    border: 1px solid #a3a3a3;
    background-color: #2245e3;
    align-self: stretch;
    margin-top: 50px;
    justify-content: center;
    align-items: center;
    padding: 14px 60px;
    font: 400 18px/150% Inter, sans-serif;
  }
  @media (max-width: 991px) {
    .div-7 {
      white-space: initial;
      margin-top: 40px;
      padding: 0 20px;
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
  </style>
