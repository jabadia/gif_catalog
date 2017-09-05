<template>
    <div id="app" class="container">
        <div class="row mb-4">
            <div class="col-12">
                <h1>Gif Catalog</h1>
                {{msg}}
            </div>
        </div>
        <gif-home></gif-home>
    </div>
</template>

<script>
    import GifHome from './components/GifHome.vue';

    export default {
        name: 'app',
        data() {
            return {
                msg: 'Welcome to Your Vue.js App!'
            }
        },
        components: {
            GifHome,
        },
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

</style>
