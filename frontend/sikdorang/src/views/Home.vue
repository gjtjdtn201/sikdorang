<template>
  <div class="home">
    <transition name="component-fade" mode="out-in">
      <component
        v-bind:is="view"
        v-on:toMainPage="changeToMainPage"
        v-on:toLoginPageOrMyPage="changeToLoginPageOrMyPage"
      ></component>
    </transition>
  </div>
</template>

<script>
// @ is an alias to /src
import MainPage from "@/components/main/MainPage.vue";
import LoginPage from "@/components/main/LoginPage.vue";

export default {
  name: "Home",
  components: {
    MainPage,
    LoginPage,
  },
  data() {
    return {
      view: MainPage,
      nowMain: true,
    };
  },
  created() {
    window.addEventListener("scroll", this.handleScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      //empty block
    },
    changeToLoginPageOrMyPage() {
      // islogin확인
      if (this.$store.state.isLogin) {
        // 마이페이지로 이동
        this.$router.push({ name: "MyPageView" });
      } else {
        this.view = LoginPage;
        this.nowMain = false;
      }
    },

    changeToMainPage() {
      this.view = MainPage;
      this.nowMain = true;
    },
  },
};
</script>

<style scoped>
.component-fade-enter-active {
  transition: all 0.5s;
}
.component-fade-enter {
  opacity: 0;
  transform: translateY(30px);
}
.home {
  text-align: center;
}
.arrow-btn {
  margin: auto;
}
</style>
