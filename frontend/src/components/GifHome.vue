<template>
    <div>
        <div class="row mb-4">
            <div class="col">
                <input type="text" placeholder="search" v-model="q">
            </div>
            <div class="col">
                <button @click="reloadPics" class="btn btn-primary">show others...</button>
            </div>
        </div>
        <div class="row">
            <gif-pic v-for="pic in pics" :key="pic.id" :pic="pic"></gif-pic>
        </div>
    </div>
</template>

<script>
    import gifPicsApi from '../services/gifPicsApi.js';
    import GifPic from './GifPic.vue';

    export default {
        data() {
            return {
                pics: [],
                q: '',
            };
        },
        watch: {
            q() {
                if (this.q) {
                    this.searchFor(this.q);
                }
                else {
                    this.reloadPics();
                }
            },
        },
        methods: {
            reloadPics() {
                gifPicsApi.getRandomPics().then(pics => {
                    this.pics = pics;
                });
            },
            searchFor(q) {
                gifPicsApi.search(q).then(pics => {
                    this.pics = pics;
                });
            }
        },
        mounted() {
            this.reloadPics();
        },
        components: {
            GifPic,
        },
    };
</script>

<style lang="less" rel="stylesheet/less">
</style>
