<template>
    <div id="app" class="container">
        <div class="row mb-4">
            <div class="col">
                <h1>Gif Catalog</h1>
                {{msg}}
            </div>
            <div class="col-auto">
                <a class="pull-right" href="/logout/">logout <b>{{user.username}}</b></a>
            </div>
        </div>
        <transition name="fade" mode="out-in">
            <keep-alive>
                <router-view></router-view>
            </keep-alive>
        </transition>
    </div>
</template>

<script>
    export default {
        name: 'app',
        data() {
            return {
                msg: 'Welcome to Your Vue.js App!',
                user: {},
            }
        },
        created() {
            this.user = window.user;
        },
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity .5s
    }

    .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
    {
        opacity: 0
    }
</style>
