public final class DamagePreview {
    private DamagePreview() {
    }

    public static int applyArmor(int baseDamage, int armor) {
        return Math.max(1, baseDamage - armor);
    }

    public static void main(String[] args) {
        System.out.println("GameRELab damage preview: " + applyArmor(42, 7));
    }
}
