<template>
    <div class="row">
        <gif-pic v-for="pic in pics" :key="pic.id" :pic="pic"></gif-pic>
    </div>
</template>

<script>
    import gifPicsApi from '../services/gifPicsApi.js';
    import GifPic from './GifPic.vue';

    export default {
        data() {
            return {
                pics: [],
            };
        },
        mounted() {
            gifPicsApi.getRandomPics().then(pics => {
                this.pics = pics;
            });
        },
        components: {
            GifPic,
        },
    };
</script>

<style lang="less" rel="stylesheet/less">
</style>
