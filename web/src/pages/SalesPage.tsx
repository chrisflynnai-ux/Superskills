import { HeroSection } from '../components/sales/HeroSection';
import { NarrativeStack } from '../components/sales/NarrativeStack';
// ReactLenis removed temporarily due to React 19 compatibility
// import ReactLenis from '@studio-freight/react-lenis';

// ASSET MANIFEST
// TODO: Reorder these slides to match the strategic narrative flow of the PDF.
// Currently attempting to follow a logical sequence if filenames contain hints, otherwise alphabetical.
const SLIDE_ASSETS = [
    "image_7ceb77aa-1a3e-4a9c-8a4c-b1e8fb41f412.png",
    "image_14b1943e-e426-4b24-8333-8d65fde6780a.png",
    "image_e4639bde-3beb-4eb0-8f70-42de3f45b061.png",
    "image_d027d571-1528-43d5-ad01-2065f91f8709.png",
    "image_dbc42d77-3088-4e09-8b23-39773b5a9039.png",
    "image_2bb597bd-5dde-469e-b45c-1be0ad1ad0f4.png",
    "image_34c1f167-f8ac-4069-a147-3cfbfc19da0c.png",
    "image_e6b98554-5d7d-4d51-8614-4f2c4374dbee.png",
    "image_60435b32-0088-4511-8f07-acd4271dbae9.png",
    "image_652328c0-46ce-47c4-8b6b-2846ef1a8f24.png",
    "image_bcf76fa2-ef76-4c72-b86c-cf56b7712571.png",
    "image_4d429fe1-67fe-4d16-8dff-36e5fdd7be10.png",
    "image_2a3e6042-7d8a-4dfa-8e9e-af460e20bdf4.png",
    "image_572cae21-3d45-458e-a4bc-a92e833671f4.png",
    "image_caec1265-bc95-467f-8d63-6df8017f6472.png",
    "image_8b8b75c9-cc9b-46f4-ad14-92ca66683600.png",
    "image_e1e51bba-08e2-45c2-847b-6f34eb01707e.png",
    "image_903933e2-a186-4186-8954-ae00f432f757.png",
    "image_1bb59120-5e15-45ed-8bc7-dbe751e1eaae.png",
    "image_aeb63366-8a4c-48bb-969c-52dcf6d6a484.png",
    "image_64e670cd-3507-4f3f-9af6-d8e07576487b.png",
    "image_aca99b92-74cf-4701-a17b-af19b7358901.png",
    "image_6d4e99a1-4127-4baa-9295-466adb69b3a5.png"
];

export default function SalesPage() {
  // Slide 1 is the Hero Background
  const heroSlide = SLIDE_ASSETS[0];
  // The rest form the stack
  const stackSlides = SLIDE_ASSETS.slice(1);

  return (
    <main className="w-full min-h-screen bg-surface font-body text-text-body antialiased">
          <HeroSection slideImage={heroSlide} />
          <NarrativeStack slides={stackSlides} />
      </main>
  );
}
